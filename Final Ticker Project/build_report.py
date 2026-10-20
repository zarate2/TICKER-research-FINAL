"""Regenerate ELV visible output and driver evidence using the same workbench engine."""
import html
import json
import re
from pathlib import Path
import model as m
ROOT=Path(__file__).resolve().parent

def table(headers,rows):
    return '| '+' | '.join(map(str,headers))+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(map(str,r))+' |\n' for r in rows)+'\n'

def number(x,n=3):return f'{x:,.{n}f}' if x is not None else 'Invalid endpoint'

def render_markdown(text):
    def inline(s):
        s=html.escape(s)
        s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<a href="\2">\1</a>',s)
        return re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    lines=text.splitlines();body=[];i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith('|') and i+1<len(lines) and lines[i+1].startswith('| ---'):
            heads=[s.strip() for s in line.strip('|').split('|')];i+=2;rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                rows.append([s.strip() for s in lines[i].strip('|').split('|')]);i+=1
            body.append('<div class="scroll"><table><thead><tr>'+''.join('<th>'+inline(x)+'</th>' for x in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>');continue
        if line.startswith('#'):
            n=len(line)-len(line.lstrip('#'));body.append(f'<h{n}>'+inline(line[n:].strip())+f'</h{n}>')
        elif line:body.append('<p>'+inline(line)+'</p>')
        i+=1
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ELV — frozen report</title><style>body{font:15px/1.6 system-ui;max-width:1200px;margin:40px auto;padding:20px;color:#173044}h1,h2,a{color:#087f74}table{border-collapse:collapse;font-size:12px;width:100%}td,th{border-bottom:1px solid #ddd;padding:8px;text-align:right;white-space:nowrap}td:first-child,th:first-child{text-align:left}.scroll{overflow:auto}h2{margin-top:40px}p{overflow-wrap:anywhere}</style><body>'+''.join(body)+'</body></html>'

def build():
    out=ROOT/'outputs';out.mkdir(exist_ok=True)
    d=m.dashboard();r=d['current'];v=r['valuation'];changed=m.run(dict(m.BASE,margin_shift=.5));cv=changed['valuation'];meta=m.metadata()
    (out/'BASE_RUN.json').write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
    parts=['# Elevance Health (ELV) — frozen model output\n',meta['basis'],
      'Origin 2025-12-31; filing published 2026-02-06; peer prices 2026-09-10; rebuilt 2026-10-19. USD millions unless specified. Shares are 220.723898 million opening common shares, not annual diluted weighted-average shares.\n',
      '## Decision and architecture\n',meta['action'],meta['limitation'],meta['eligibility'],
      table(['ELV case','Value/opening share','2030 operating profit','2030 FCFE','Story'],[[k,number(x['valuation']['per_share'],2) if x['valuation'] else 'Withheld',number(x['rows'][-1]['ebit']),number(x['rows'][-1]['fcfe']),x['story']] for k,x in d['scenarios'].items()]),
      'Cases are conditional scenarios, not confidence intervals. Do not average the later-dated peer range with this historical-origin model.\n',
      '## Direct equity valuation\n',table(['Component','Value'],[[k,number(v[k],6)] for k in ['pv_flows','terminal_cash','terminal_value','pv_terminal','equity','shares','per_share','terminal_share']]),
      'FCFE = CFO − capex − scheduled net debt repayment, before distributions and liquidity-only revolver movements. Signed negative interim flows remain in the DCF. Terminal FCFE adds back 2030 net repayment, then grows at g; perpetual debt refinancing and unmodeled statutory-capital reinvestment are material assumptions. No second debt subtraction or consolidated cash/investment addition.\n',
      '## Reverse DCF\n',f"At the 2025-12-31 unadjusted close of $350.55, implied cost of equity is **{d['reverse']['ke']:.4f}%** with base operations and terminal growth. The FY2025 filing was published later; this is a retrospective comparison, not a contemporaneous backtest.\n",
      '## Five-year statements\n',table(['Assumption']+[str(x['year']) for x in r['rows']],[[label]+[f'{x*100:.2f}%' for x in r['annual_assumptions'][key]] for label,key in [('Revenue growth','growth'),('Blended gross margin','margin'),('Cash expense / gross profit','cash_opex_ratio')]])]
    for name,fields in m.GROUPS.items():parts+=['### '+name+'\n',table(['USD millions']+[str(x['year'])+'E' for x in r['rows']],[[label]+[number(x[key]) for x in r['rows']] for label,key in fields])]
    parts+=['## Filing reconciliation and forecast checks\n',table(['Check','Pass','Gap / headroom'],[[x['name'],x['pass'],number(x['gap'],8)] for x in r['checks']]),'Accounting tolerance $0.000001m. No balancing plug. A funding check is not a statutory-capital test.\n',
      '## Cost of equity / terminal growth grid\n',table(['Cost of equity / g','1%','1.5%','2%','2.5%','3%','3.5%'],[[x['ke']]+[number(y,2) for y in x['values']] for x in d['grid']]),'Values are dollars per opening common share. Terminal growth is extrapolated without an explicit capital-retention schedule.\n','## One-at-a-time sensitivity\n']
    for band in ['Full control range','Alternative local range']:
        items=[x for x in d['sensitivity'] if x['band']==band];items.sort(key=lambda x:x['value_span'] if x['value_span'] is not None else -1,reverse=True)
        parts+=['### '+band+'\n',table(['Driver','Low → high input','Profit span','FCFE span','Value/share span'],[[x['label'],f"{x['low_input']:.3f} → {x['high_input']:.3f} {x['units']}",number(x['ebit_span']),number(x['fcfe_span']),number(x['value_span'])] for x in items])]
        for key in ['ebit_span','fcfe_span','value_span']:
            ranked=sorted([x for x in items if x[key] is not None],key=lambda x:x[key],reverse=True)
            parts.append(key+' leaders: '+', '.join(x['label'] for x in ranked[:3])+'.\n')
    c=d['comps']
    parts+=['Invalid endpoints are excluded from all output rankings. Results show absolute endpoint spans; signs and annual details are retained in BASE_RUN.json.\n',
      '## ELV comparable-company reference — September 10, 2026\n',table(['Ticker','Policy','Close','FY2025 total GAAP diluted EPS','P/E','Implied ELV/share'],[[x['ticker'],x['policy']]+[number(x[k],4) for k in ['price','eps','pe','implied_elv']] for x in c['rows']]),
      f"Peer range **${c['pe_range'][0]:.2f}–${c['pe_range'][1]:.2f}**; median reference **${c['median_price']:.2f}**. Removing UNH leaves ${c['leave_one_out'][0]['value']:.2f}; removing CI leaves ${c['leave_one_out'][1]['value']:.2f}. No debt/cash adjustment belongs in P/E. No enterprise multiple is asserted for this insurer architecture.\n",
      'UNH/Optum and CI/Evernorth differ in payer mix, services and earnings quality. The small qualified set and the later price date limit the comparison; do not average with DCF.\n',
      '## Exact live demonstration\n',table(['Metric','Base','Margin shift +0.50 pp','Difference'],[[k,number(r['rows'][-1][k],6),number(changed['rows'][-1][k],6),number(changed['rows'][-1][k]-r['rows'][-1][k],6)] for k in ['ebit','fcfe','cash']]+[['value/share',number(v['per_share'],6),number(cv['per_share'],6),number(cv['per_share']-v['per_share'],6)]]),
      'Cash-error diagnostic: FY2026 cash is reduced by $100m without changing cash flows. Balance-sheet and cash-flow gaps both become −$100m and valuation is withheld. Reset restores the base.\n',
      '## Source map\n']
    for s in m.SOURCES.values():parts.append(f"- [{s['title']}]({s['url']}): {s['locator']} Period {s['period']}; checked {s['accessed']}.\n")
    parts+=['See MODEL_GUIDE.md for fixed choices and normalization; SUBMISSION_CHECKLIST.md for unresolved course and human evidence.\n']
    report='\n'.join(parts);(out/'BASE_REPORT.md').write_text(report);(out/'BASE_REPORT.html').write_text(render_markdown(report))
    audit=['# ELV assumption challenge record\n\nAI-assisted draft. Actual partner name, date and challenges remain in HUMAN_RECORDS.md.\n']
    for k,s in m.DRIVERS.items():audit.append(f'## {s[0]}\n\nValue: {s[1]} {s[5]}; bounds {s[2]}–{s[3]}.\n\nBasis: {s[6]}\n\nChallenge: {s[7]}\n\nEvidence that changes it: {s[8]}\n')
    audit+=['## Locked choices needing review\n\nCash floor 9,491 is a consolidated liquidity proxy, not regulatory capital. Revolver capacity 5,000 assumes renewal at September 2030 and no covenant breach. Dividends 1,529 assume parent cash availability. PP&E D&A 979/4679 and intangible amortization 628 follow the prior lab asset schedules; 979+628 does not reconcile to the 1,546 historical CFO addback. Flat investment assets, other liabilities and NCI, no OCI/acquisitions, and no separate stock compensation/dilution forecast simplify the statements. Opening shares 220.723898 value the opening equity claim; they are not a forecast EPS denominator. No automatic tax benefit on losses. Each simplification must be challenged against new filings, statutory accounts and parent cash/debt schedules.\n']
    (ROOT/'records/ASSUMPTION_CHALLENGE.md').write_text('\n'.join(audit))
    print('Rebuilt ELV BASE_REPORT.md, BASE_REPORT.html, BASE_RUN.json and ASSUMPTION_CHALLENGE.md')
if __name__=='__main__':build()
