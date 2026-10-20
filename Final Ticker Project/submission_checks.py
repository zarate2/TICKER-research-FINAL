"""Check the active ELV package. Technical PASS never means course submission complete."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import model as m
ROOT=Path(__file__).resolve().parent


def main():
    lines=['ELV local package check: '+datetime.now(timezone.utc).isoformat()];failures=[]
    def check(label,ok):
        lines.append(('PASS: ' if ok else 'FAIL: ')+label)
        if not ok:failures.append(label)
    required=['START_HERE.md','README.md','MODEL_GUIDE.md','COMMITTEE_MEMO.md','RESEARCH_EVOLUTION.md','SUBMISSION_CHECKLIST.md','VIDEO_1_SCRIPT.md','VIDEO_2_SCRIPT.md','VIDEO_PLAYBOOK.md','model.py','elv_forecast.py','app.py','index.html','test_model.py','cold_run.py','build_report.py','freeze_manifest.py','Launch Workbench.command','outputs/BASE_REPORT.html','outputs/BASE_REPORT.md','outputs/BASE_RUN.json','research/SOURCES.json','research/HISTORICAL_INPUTS.json','research/PEER_POLICY.md','research/ASSIGNMENT.md','records/HUMAN_RECORDS.md','records/AI_USE_AND_VALIDATION.md','records/AI_DIRECTIONAL_PRECOMMIT.md','records/ASSUMPTION_CHALLENGE.md']
    for name in required:check('Required file '+name,(ROOT/name).is_file() and (ROOT/name).stat().st_size>0)
    current=m.dashboard();v=current['current']['valuation'];demo=m.run(dict(m.BASE,margin_shift=.5))['valuation']
    check('Engine identifies Elevance Health / ELV',current['meta']['ticker']=='ELV' and current['meta']['company']=='Elevance Health, Inc.')
    check('Every ELV reference case passes',all(r['valid'] for r in current['scenarios'].values()))
    check('Filing mappings all reconcile',all(x['pass'] for x in m.checks_base()))
    check('Peer universe is ELV, UNH, CI',[x['ticker'] for x in m.comps()['rows']]==['ELV','UNH','CI'])
    try:
        saved=json.loads((ROOT/'outputs/BASE_RUN.json').read_text())
        check('Saved dashboard exactly matches current ELV engine',saved==json.loads(json.dumps(current)))
    except (OSError,ValueError) as e:check('Readable ELV JSON output: '+str(e),False)
    texts={name:(ROOT/name).read_text() for name in required if (ROOT/name).is_file() and (name.endswith('.md') or name.endswith('.html'))}
    active=['START_HERE.md','MODEL_GUIDE.md','COMMITTEE_MEMO.md','VIDEO_1_SCRIPT.md','VIDEO_2_SCRIPT.md','VIDEO_PLAYBOOK.md','SUBMISSION_CHECKLIST.md','index.html','outputs/BASE_REPORT.html','outputs/BASE_REPORT.md']
    for name in active:
        s=texts.get(name,'')
        check(name+' identifies ELV','ELV' in s)
        check(name+' has no superseded company calculations',not any(x in s for x in ['179.53','188.17','232.53','Asbury','New vehicle gross margin','GPI','SAH']))
    for name in ['START_HERE.md','MODEL_GUIDE.md','COMMITTEE_MEMO.md','VIDEO_1_SCRIPT.md','VIDEO_2_SCRIPT.md','VIDEO_PLAYBOOK.md','outputs/BASE_REPORT.md']:
        check(name+' uses the current base result',f"{v['per_share']:.2f}" in texts.get(name,''))
    for name in ['START_HERE.md','VIDEO_2_SCRIPT.md','VIDEO_PLAYBOOK.md']:
        check(name+' uses the current margin-demo result',f"{demo['per_share']:.2f}" in texts.get(name,''))
    check('Assignment insurer exclusion preserved','insurers' in texts.get('research/ASSIGNMENT.md','') and 'not eligible' in texts.get('research/ASSIGNMENT.md',''))
    check('Checklist explicitly flags architecture departure','Departure: instructor acceptance unresolved' in texts.get('SUBMISSION_CHECKLIST.md',''))
    check('Evidence map contains ELV filing and dated origin price','ELV_K' in m.SOURCES and m.SOURCES['ELV_ORIGIN_PRICE']['value']==350.55)
    hist=json.loads((ROOT/'research/HISTORICAL_INPUTS.json').read_text())
    check('Saved history matches active filing inputs',hist['historical']==m.HIST and hist['assets']==m.ASSETS and hist['liabilities']==m.LIABS)
    check('Fail-loud diagnostics withhold value',all(m.run(fault=f)['valuation'] is None for f in ['cash','terminal']))
    lines+=['TECHNICAL PACKAGE: '+('FAIL' if failures else 'PASS'),
            'COURSE SUBMISSION: INCOMPLETE — instructor disposition for ELV/FCFE/EV-multiple and training-proof departures, original checkpoint/receipt, genuine AI-off prediction, partner evidence, recordings, corrected transcripts, access checks and submission receipt remain pending.',
            'No upload, instructor approval, human precommit or completed submission is asserted.']
    (ROOT/'records/SUBMISSION_CHECKS.log').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines));return 1 if failures else 0
if __name__=='__main__':sys.exit(main())
