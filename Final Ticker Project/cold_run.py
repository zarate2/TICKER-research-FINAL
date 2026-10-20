"""Fresh environment and copy; no packages installed. Logs actual tests and HTTP behavior."""
from datetime import datetime,timezone
import json
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
import urllib.error
import venv
ROOT=Path(__file__).resolve().parent

def main():
    log=['Cold run started: '+datetime.now(timezone.utc).isoformat(),'Host interpreter: '+sys.version,'No third-party dependencies; no package/network downloads.']
    success=False
    try:
        with tempfile.TemporaryDirectory(prefix='elv_cold_') as temp:
            temp=Path(temp);folder=temp/'project'
            shutil.copytree(ROOT,folder,ignore=shutil.ignore_patterns('__pycache__','.venv','*.zip'))
            venv.EnvBuilder(with_pip=False,system_site_packages=False).create(temp/'venv')
            python=temp/'venv'/'bin'/'python'
            if not python.exists():python=temp/'venv'/'Scripts'/'python.exe'
            for cmd in [[str(python),'-m','unittest','-v'],[str(python),'build_report.py'],[str(python),'submission_checks.py']]:
                completed=subprocess.run(cmd,cwd=folder,text=True,capture_output=True,timeout=45)
                log+=['COMMAND: '+' '.join(cmd),completed.stdout,completed.stderr,'EXIT: '+str(completed.returncode)]
                if completed.returncode:raise RuntimeError('Cold command failed')
            with socket.socket() as sock:
                sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
            server=subprocess.Popen([str(python),'app.py','--no-browser','--port',str(port)],cwd=folder,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            try:
                root=f'http://127.0.0.1:{port}'
                for _ in range(50):
                    try:
                        with urllib.request.urlopen(root+'/health',timeout=1) as reply:
                            if reply.status==200:break
                    except (OSError,urllib.error.URLError):time.sleep(.1)
                else:raise RuntimeError('Cold local server unavailable')
                with urllib.request.urlopen(root) as reply: page=reply.read().decode()
                assert 'Driver panel' in page and 'Inject cash error' in page and 'ELV · Equity' in page
                assert 'ABG' not in page
                with urllib.request.urlopen(root+'/api/base') as reply:base=json.load(reply)
                assert abs(base['current']['valuation']['per_share']-365.238953959506)<1e-6
                def post(body):
                    request=urllib.request.Request(root+'/api/run',json.dumps(body).encode(),{'Content-Type':'application/json'})
                    with urllib.request.urlopen(request) as reply:return json.load(reply)
                changed=post({'inputs':dict(base['current']['inputs'],margin_shift=.5)})
                assert abs(changed['current']['valuation']['per_share']-378.818002947429)<1e-6
                broken=post({'inputs':base['current']['inputs'],'fault':'cash'})
                assert not broken['current']['valid'] and broken['current']['valuation'] is None
                terminal=post({'inputs':base['current']['inputs'],'fault':'terminal'})
                assert not terminal['current']['valid'] and terminal['current']['valuation'] is None
                restored=post({'inputs':base['current']['inputs']})
                assert restored['current']==base['current']
                try:post({'inputs':dict(base['current']['inputs'],growth=999)})
                except urllib.error.HTTPError as error:assert error.code==400
                else:raise AssertionError('Bad input not rejected')
                log+=['PASS: fresh server health and HTML served.','PASS: base = $365.238953959506; changed input = $378.818002947429.',
                      'PASS: cash and terminal diagnostics suppress valuation; reset recovers exact base.',
                      'PASS: out-of-bounds HTTP input returns 400.',
                      'PASS: frozen report generation in the fresh environment.',
                      'UI note: this automated cold run tests HTTP and model behavior; graphical interaction is a separate manual/Chrome check.']
            finally:
                server.terminate();output=server.communicate(timeout=5)[0];log+=['SERVER OUTPUT:',output]
            success=True
    except Exception as error:
        log.append('FAILED: '+repr(error))
    log.append('FINISHED: '+datetime.now(timezone.utc).isoformat())
    log.append('RESULT: '+('PASS' if success else 'FAIL'))
    path=ROOT/'records/COLD_RUN.log';path.write_text('\n'.join(log)+'\n');print('\n'.join(log))
    return 0 if success else 1
if __name__=='__main__':sys.exit(main())
