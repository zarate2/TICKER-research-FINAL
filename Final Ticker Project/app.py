"""Local-only workbench. Run python3 app.py; stop with Ctrl+C."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
import webbrowser
import model

ROOT=Path(__file__).resolve().parent
class Handler(BaseHTTPRequestHandler):
    def send(self,body,status=200,kind='application/json; charset=utf-8'):
        data=body.encode() if isinstance(body,str) else body
        self.send_response(status); self.send_header('Content-Type',kind)
        self.send_header('Content-Length',str(len(data))); self.send_header('Cache-Control','no-store')
        self.end_headers(); self.wfile.write(data)
    def do_GET(self):
        if self.path in ['/','/index.html']:
            self.send((ROOT/'index.html').read_bytes(),kind='text/html; charset=utf-8')
        elif self.path=='/api/base': self.send(json.dumps(model.dashboard(),allow_nan=False))
        elif self.path=='/health': self.send('{"status":"ok"}')
        elif self.path=='/favicon.ico': self.send(b'',204)
        else: self.send('{"error":"Not found"}',404)
    def do_POST(self):
        if self.path!='/api/run': return self.send('{"error":"Not found"}',404)
        try:
            length=int(self.headers.get('Content-Length','0'))
            if not 0<length<=20000: raise ValueError('Invalid request size')
            payload=json.loads(self.rfile.read(length))
            if not isinstance(payload,dict): raise ValueError('Expected input object')
            fault=payload.get('fault')
            if fault not in [None,'cash','terminal']: raise ValueError('Unknown diagnostic')
            result=model.dashboard(payload.get('inputs',model.BASE),fault)
            self.send(json.dumps(result,allow_nan=False))
        except (ValueError,TypeError,KeyError) as e:
            self.send(json.dumps({'error':str(e)}),400)
    def log_message(self,fmt,*args): pass

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port',type=int,default=8765)
    parser.add_argument('--no-browser',action='store_true')
    args=parser.parse_args()
    try: server=ThreadingHTTPServer(('127.0.0.1',args.port),Handler)
    except OSError as exc:
        raise SystemExit(f'Could not start: {exc}\nTry python3 app.py --port 8766')
    url=f'http://127.0.0.1:{args.port}'
    print(f'ELV workbench running at {url}\nKeep this Terminal open. Ctrl+C stops the app.',flush=True)
    if not args.no_browser: threading.Timer(.5,lambda:webbrowser.open(url)).start()
    try: server.serve_forever()
    except KeyboardInterrupt: print('\nStopped.')
    finally: server.server_close()
if __name__=='__main__': main()
