"""ELV workbench: linked insurer statements and conditional FCFE equity valuation.
Python 3.9+, standard library. USD millions; shares in millions.
"""
from copy import deepcopy
import json
import math
from pathlib import Path
import elv_forecast as engine

ROOT = Path(__file__).resolve().parent
SOURCES = json.loads((ROOT/'research/SOURCES.json').read_text())
ASSETS = dict(cash=9491., fixed_current=25884., equity_securities=740.,
              premium_receivables=10073., self_funded_receivables=5162., other_receivables=6307.,
              other_current=5344., fixed_long=1121., other_investments=10839., ppe=4679.,
              goodwill=28344., intangibles=11200., other_noncurrent=2310.)
LIABS = dict(claims=17084., policyholder=3632., unearned=1493., payables=7322.,
             short_debt=150., current_debt=1099., other_current=10255., long_debt=30797.,
             future_benefits=145., deferred_tax=2110., other_noncurrent=3381.)
HIST = dict(revenue=197584., premiums=164639., product_revenue=24470., fees=8475.,
            benefits=148223., products=21178., opex=20984., investment_income=2194.,
            financial_losses=653., interest=1402., amort=628., pretax=6710., tax=1049.,
            net_income=5661., common_income=5662., nci_loss=1., eps=25.21,
            assets=121494., liabilities=77468., equity=43882., nci=144.,
            cfo=4290., cfi=-1344., cff=-1738., fx=-5., opening_cash=8288.,
            shares=220.723898, depreciation=94., software_amort=885., cf_da=1546.)
# label, base, lower, upper, step, units, basis, challenge, evidence for revision
DRIVERS = {
 'growth': ('Operating revenue growth',3.,0.,6.,.1,'%', 'Lab 10 base 3%; FY2025 operating revenue grew 12.77%, influenced by mix and pricing. 0–6% is an analyst scenario range.', 'One aggregate driver does not separate membership, pricing, premiums and Carelon.', 'Membership, premium yields, Medicaid rate adequacy and Carelon external revenue.'),
 'margin_shift': ('Blended gross margin shift',0.,-1.,1.,.05,'percentage points', 'Shift all five base margins: 14.3, 14.5, 14.7, 14.8, 14.8%. FY2025 blended margin 14.2638%. Bounds are analyst stresses.', 'This is not medical benefit ratio: benefits and product costs are blended over total operating revenue.', 'Medical utilization, pricing, payer mix and Carelon product economics.'),
 'expense_shift': ('Cash expense / gross profit shift',0.,-2.,2.,.1,'percentage points', 'Shift base expense ratios 71.2, 70.8, 70.4, 70.0, 70.0%. FY2025 proxy is (20984−979)/28183 =71.1989%.', 'Efficiency gains may be offset by staffing, compliance or technology costs.', 'Reported operating expenses, identified noncash items and sustainable efficiency evidence.'),
 'claims_days': ('Medical claims payment timing',17084/148223*365,38.,48.,.1,'days', 'FY2025 ending claims / annual benefits ×365 =42.07; prior lab history 2024=45.05 and 2023=47.30. Bounds are stresses.', 'Ending balance is not an actuarial adequacy test; slower payment is not better underwriting.', 'Claims payment patterns, reserve development and statutory filings.'),
 'capex': ('Annual capital expenditure',1116.,900.,1500.,25.,'$m', 'FY2025 capex 1116; prior lab FY2024=1256, FY2023=1296. Bounds test underinvestment and higher technology spend.', 'Flat spending may understate replacement and growth requirements.', 'Capital commitments and software investment needed to support services growth.'),
 'tax': ('Normalized tax rate',24.,20.,28.,.5,'%', '24% judgment replaces FY2025 effective rate 15.63%; tax benefits are not assumed to repeat.', 'Cash taxes may differ from book tax; losses get no automatic tax asset.', 'Tax-note changes and a normalized cash-tax reconciliation.'),
 'investment_income': ('Normalized investment income',1796.,1400.,2400.,25.,'$m', '2194 reported less 398 equity-method earnings =1796. Portfolio balances held flat.', 'Remainder is assumed cash; flat assets and income miss reinvestment, duration and growth.', 'Portfolio yields, reinvestment cash flows and upstream cash availability.'),
 'debt_rate': ('Debt interest rate',1402/32046*100,3.5,6.5,.1,'%', 'FY2025 interest / closing debt =4.375%; applied to opening forecast debt. Not a market quote.', 'Closing debt is not average debt; refinancing cost may differ.', 'Debt maturity, coupon and refinancing schedules.'),
 'repayment': ('Annual net debt repayment',1000.,0.,2000.,100.,'$m', 'Lab 10 judgment; assumes other maturities are refinanced and scheduled net paydown stops after 2030.', 'A perpetual no-paydown terminal is a classroom simplification.', 'Parent debt maturities, leverage targets and refinancing access.'),
 'buyback': ('Annual buybacks',2605.,0.,6000.,100.,'$m', 'Hold FY2025 repurchases at 2605; dividends fixed at 1529. Upper bound deliberately tests funding strain.', 'Payouts can exhaust liquidity; no execution-price/share-reduction schedule is modeled.', 'Parent liquidity, regulated dividends, repurchase plans and authorization.'),
 'ke': ('Cost of equity',10.,8.,12.,.1,'%', 'Lab 10 required-return judgment. 8–12% is a sensitivity interval, not an estimated confidence interval.', 'Insurer equity risk needs a dated capital-market calibration.', 'Risk-free yield, equity risk premium, beta and capital/underwriting risk.'),
 'terminal_growth': ('Terminal growth',2.5,1.,3.5,.1,'%', 'Lab 10 mature nominal growth judgment. All rates below the cost-of-equity bounds.', 'Extrapolation does not explicitly fund statutory capital growth or portfolio growth.', 'Long-run growth, required capital and subsidiary dividend capacity.'),
}
BASE = {k:s[1] for k,s in DRIVERS.items()}
LOCAL = dict(growth=.5,margin_shift=.25,expense_shift=.5,claims_days=1.,capex=100.,tax=1.,investment_income=100.,debt_rate=.5,repayment=250.,buyback=500.,ke=.25,terminal_growth=.25)
SCENARIOS = {'Low':dict(growth=2.,margin_shift=-.5,expense_shift=1.,capex=1300.,ke=11.,terminal_growth=2.),
             'Base':{},'High':dict(growth=4.,margin_shift=.5,expense_shift=-.5,ke=9.,terminal_growth=3.)}
STORIES = {'Low':'Slower revenue, medical/product cost pressure, weaker efficiency and higher required return.',
           'Base':'Modest growth and gradual margin/expense recovery with unchanged cash and capital simplifications.',
           'High':'Stronger growth, better blended margin and efficiency, with a lower required return.'}
GROUPS = {
 'Income statement': [('Operating revenue','revenue'),('Benefit expense','benefits'),('Product costs','products'),('Blended gross profit','gross_profit'),('Cash operating expense','cash_opex'),('PP&E depreciation / amortization','ppe_da'),('Other intangible amortization','amort'),('Operating income after D&A','ebit'),('Normalized investment income','investment_income'),('Interest expense','interest'),('Pretax income','pretax'),('Tax expense','tax'),('Net income assigned to common','net_income')],
 'Balance sheet': [('Cash','cash'),('Receivables','receivables'),('PP&E','ppe'),('Investments','investments'),('Intangibles','intangibles'),('Other assets incl. goodwill','other_assets'),('TOTAL ASSETS','assets'),('Medical claims payable','claims'),('Debt','debt'),('Revolver','revolver'),('Other liabilities','other_liabilities'),('TOTAL LIABILITIES','liabilities'),('Common equity','equity'),('Noncontrolling interests','nci')],
 'Cash flow and equity cash flow': [('Net income','net_income'),('PP&E D&A addback','ppe_da'),('Intangible amortization addback','amort'),('Receivables increase (cash use)','receivables_change'),('Other working-capital increase (cash use)','other_wc_change'),('Claims increase (cash source)','claims_change'),('CASH FROM OPERATIONS','cfo'),('Capex / investing cash flow','cfi'),('Net debt repayment (cash use)','repayment'),('FCFE before distributions and revolver','fcfe'),('Buybacks (cash use)','buyback'),('Dividends (cash use)','dividend'),('Revolver draw / (repayment)','revolver_change'),('CASH FROM FINANCING','cff'),('Opening cash','opening_cash'),('Closing cash','cash')]
}

def identity(name,gap,tolerance=1e-6):
    return dict(name=name,gap=gap,tolerance=tolerance,**{'pass':math.isfinite(gap) and abs(gap)<=tolerance})

def checks_base():
    h=HIST; o=engine.OPENING
    grouped_assets=dict(cash=ASSETS['cash'],receivables=sum(ASSETS[k] for k in ['premium_receivables','self_funded_receivables','other_receivables']),ppe=ASSETS['ppe'],investments=sum(ASSETS[k] for k in ['fixed_current','equity_securities','fixed_long','other_investments']),intangibles=ASSETS['intangibles'],other_assets=sum(ASSETS[k] for k in ['other_current','goodwill','other_noncurrent']))
    grouped_liabs=dict(claims=LIABS['claims'],debt=sum(LIABS[k] for k in ['short_debt','current_debt','long_debt']),other_liabilities=sum(LIABS[k] for k in ['policyholder','unearned','payables','other_current','future_benefits','deferred_tax','other_noncurrent']),equity=h['equity'],nci=h['nci'])
    gaps={'Filing assets aggregation':sum(ASSETS.values())-h['assets'],
          'Filing liabilities aggregation':sum(LIABS.values())-h['liabilities'],
          'Filing balance sheet':h['assets']-h['liabilities']-h['equity']-h['nci'],
          'Filing operating revenue':h['premiums']+h['product_revenue']+h['fees']-h['revenue'],
          'Filing pretax income':h['revenue']+h['investment_income']-h['financial_losses']-h['benefits']-h['products']-h['opex']-h['interest']-h['amort']-h['pretax'],
          'Filing net income':h['pretax']-h['tax']-h['net_income'],
          'Filing common income':h['net_income']+h['nci_loss']-h['common_income'],
          'Filing cash roll-forward incl. FX':h['opening_cash']+h['cfo']+h['cfi']+h['cff']+h['fx']-ASSETS['cash']}
    gaps.update({'Opening '+k+' traces to filing':o[k]-v for k,v in dict(grouped_assets,**grouped_liabs).items()})
    gaps['Opening revenue traces to filing']=o['revenue']-h['revenue']
    gaps['Share denominator traces to filing']=engine.ASSUMPTIONS['shares']-h['shares']
    return [identity(k,v) for k,v in gaps.items()]

def validate(a):
    if not isinstance(a,dict) or set(a)!=set(BASE):raise ValueError('Unknown or missing ELV driver; locked fields cannot be edited.')
    for k,v in a.items():
        s=DRIVERS[k]
        if isinstance(v,bool) or not isinstance(v,(float,int)) or not math.isfinite(v) or not s[2]-1e-9<=v<=s[3]+1e-9:
            raise ValueError(f'{s[0]} must be finite and between {s[2]} and {s[3]} {s[5]}')
    if a['terminal_growth']>=a['ke']:raise ValueError('Terminal growth must be below cost of equity.')
    if not all(c['pass'] for c in checks_base()):raise ValueError('ELV filing reconciliation failed; valuation refused.')

def assumptions(a):
    p=deepcopy(engine.ASSUMPTIONS)
    p.update(growth=[a['growth']/100]*5,margin=[x+a['margin_shift']/100 for x in p['margin']],
             cash_opex_ratio=[x+a['expense_shift']/100 for x in p['cash_opex_ratio']],
             claims_to_benefits=a['claims_days']/365,capex=a['capex'],tax=a['tax']/100,
             investment_income=a['investment_income'],debt_rate=a['debt_rate']/100,
             net_repayment=a['repayment'],buyback=a['buyback'],ke=a['ke']/100,terminal_growth=a['terminal_growth']/100)
    return p

def row_checks(r,p):
    headroom=min(r['cash']-p['minimum_cash'],p['revolver_limit']-r['revolver'],r['revolver'])
    checks=[identity(f"{r['year']} balance sheet",r['assets']-r['liabilities']-r['equity']-r['nci']),
      identity(f"{r['year']} cash flow ties to cash",r['cash']-r['opening_cash']-r['cfo']-r['cfi']-r['cff']),
      identity(f"{r['year']} FCFE cash bridge",r['fcfe']-(r['cfo']-r['capex']-r['repayment']))]
    checks.append(dict(name=f"{r['year']} liquidity / revolver",gap=headroom,tolerance=1e-6,**{'pass':headroom>=-1e-6}))
    checks.append(dict(name=f"{r['year']} nonnegative assets / debt",gap=min(r[k] for k in ['ppe','intangibles','debt','claims']),tolerance=0.,**{'pass':min(r[k] for k in ['ppe','intangibles','debt','claims'])>=0}))
    checks.append(dict(name=f"{r['year']} finite outputs",gap=0.,**{'pass':all(math.isfinite(v) for v in r.values() if isinstance(v,(float,int)))}))
    return checks

def equity_dcf(flows,ke,g,terminal_cash,shares):
    if not flows or not all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) for v in [*flows,ke,g,terminal_cash,shares]):raise ValueError('Non-finite or missing DCF input.')
    if not -1<g<ke or shares<=0 or terminal_cash<=0:raise ValueError('Invalid equity DCF boundary or terminal cash flow.')
    pv_flows=sum(f/(1+ke)**t for t,f in enumerate(flows,1)) # Signed funding needs retained.
    terminal_value=terminal_cash/(ke-g);pv_terminal=terminal_value/(1+ke)**len(flows)
    equity=pv_flows+pv_terminal
    return dict(pv_flows=pv_flows,terminal_cash=terminal_cash,terminal_value=terminal_value,pv_terminal=pv_terminal,
                equity=equity,shares=shares,per_share=equity/shares,terminal_share=pv_terminal/equity if equity else None,
                bridge_gap=equity-pv_flows-pv_terminal)

def run(a=None,fault=None):
    a=deepcopy(BASE if a is None else a);validate(a)
    if fault not in [None,'cash','terminal']:raise ValueError('Unknown diagnostic.')
    p=assumptions(a);rows=engine.project(p,validate=False)
    if fault=='cash':rows[0]['cash']-=100.
    for r in rows:
        r['assets'],r['liabilities'],_=engine.totals(r);r['ebit']=r['operating_income']
    checks=checks_base()+[c for r in rows for c in row_checks(r,p)]
    if fault=='terminal':checks.append(dict(name='Terminal growth equals cost of equity (diagnostic)',gap=0.,**{'pass':False}))
    warnings=[]
    if a['margin_shift']<-.5 or a['margin_shift']>.5 or abs(a['expense_shift'])>1:
        warnings.append('Margin / expense assumption outside the selected review band; this is a stress case.')
    if not 42<=a['claims_days']<=47.5:warnings.append('Claims timing outside the approximate 2023–2025 reference band; investigate payment timing and reserve adequacy.')
    if any(r['revolver']>1e-6 for r in rows):warnings.append('Revolver funding is required; valuation excludes liquidity-only revolver proceeds. Confirm repayment and September 2030 facility renewal.')
    v=None
    terminal_cash=(rows[-1]['fcfe']+rows[-1]['repayment'])*(1+p['terminal_growth'])
    checks.append(dict(name='Positive final and terminal FCFE',gap=min(rows[-1]['fcfe'],terminal_cash),**{'pass':rows[-1]['fcfe']>0 and terminal_cash>0}))
    if all(c['pass'] for c in checks):
        v=equity_dcf([r['fcfe'] for r in rows],p['ke'],p['terminal_growth'],terminal_cash,p['shares'])
        checks.append(identity('Direct equity valuation reconciliation',v['bridge_gap']))
    return dict(inputs=a,annual_assumptions=p,rows=rows,checks=checks,valid=all(c['pass'] for c in checks),warnings=warnings,valuation=v)

def scenarios():return {k:dict(run(dict(BASE,**v)),story=STORIES[k]) for k,v in SCENARIOS.items()}

def sensitivity(a):
    result=[]
    for k,s in DRIVERS.items():
        for band,lo,hi in [('Full control range',s[2],s[3]),('Alternative local range',max(s[2],a[k]-LOCAL[k]),min(s[3],a[k]+LOCAL[k]))]:
            low,high=[run(dict(a,**{k:x})) for x in [lo,hi]]
            def out(r):return dict(ebit=r['rows'][-1]['ebit'] if r['valid'] else None,fcfe=r['rows'][-1]['fcfe'] if r['valid'] else None,value=r['valuation']['per_share'] if r['valuation'] else None)
            x,y=out(low),out(high);item=dict(driver=k,label=s[0],band=band,low_input=lo,high_input=hi,units=s[5],low=x,high=y,valid=low['valid'] and high['valid'])
            for key in ['ebit','fcfe','value']:item[key+'_span']=abs(y[key]-x[key]) if x[key] is not None and y[key] is not None else None
            result.append(item)
    return result

def reverse_dcf(a,price=350.55):
    # Retrospective price-date match; the FY2025 filing was published later.
    lo,hi=DRIVERS['ke'][2:4]
    def f(k):
        v=run(dict(a,ke=k))['valuation'];return v['per_share'] if v else None
    lv,hv=f(lo),f(hi)
    if lv is None or hv is None or not hv<=price<=lv:return dict(solved=False,target=price,message='No solution within the defended 8–12% cost-of-equity bounds.')
    for _ in range(70):
        mid=(lo+hi)/2;val=f(mid)
        if abs(val-price)<1e-8:break
        if val>price:lo=mid
        else:hi=mid
    return dict(solved=True,target=price,ke=mid,value=val,message='Retrospective implied cost of equity at the December 31, 2025 close; later filing evidence, not a contemporaneous backtest.')

def comps():
    rows=[dict(ticker='ELV',price=416.54,eps=25.21,policy='TARGET'),dict(ticker='UNH',price=388.28,eps=13.23,policy='QUALIFY'),dict(ticker='CI',price=280.91,eps=22.18,policy='QUALIFY')]
    for r in rows:r['pe']=r['price']/r['eps'];r['implied_elv']=r['pe']*rows[0]['eps']
    peers=rows[1:];values=[r['implied_elv'] for r in peers]
    return dict(rows=rows,pe_range=sorted(values),median_price=sum(values)/2,price_date='2026-09-10',earnings_period='FY2025 total GAAP diluted EPS',leave_one_out=[dict(removed='UNH',remaining='CI',value=values[1]),dict(removed='CI',remaining='UNH',value=values[0])])

def metadata():
    return dict(ticker='ELV',company='Elevance Health, Inc.',valuation_date='2025-12-31',filing_date='2026-02-06',market_reference_date='2026-09-10',built='2026-10-19',price=350.55,
      units='USD millions, except dollars per share and million shares',user='Buy-side analyst / portfolio manager; fund has no position',horizon='Five forecast years 2026–2030; 12–24 month monitoring',
      basis='Retrospective FY2025-base exercise using the subsequently published 2025 10-K. September 10, 2026 prices are separately dated references; no same-date upside or current recommendation is claimed.',
      action='WATCH / DEFER — analyst draft; validate medical-cost recovery, regulated capital and parent distribution capacity.',
      eligibility='The supplied Project 1 brief excludes insurers and requires FCFF/WACC and enterprise multiples. This requested ELV/FCFE build is a disclosed departure; instructor acceptance is unresolved.',
      limitation='Consolidated FCFE is a proxy, not verified cash distributable from regulated subsidiaries. A fixed cash floor does not test statutory capital adequacy.')

def dashboard(a=None,fault=None):
    a=BASE if a is None else a;r=run(a,fault)
    out=dict(current=r,base=run(),drivers=DRIVERS,sources=SOURCES,meta=metadata(),groups=GROUPS)
    if not r['valid']:return out
    grid=[]
    for ke in [8.,9.,10.,11.,12.]:
        grid.append(dict(ke=ke,values=[(lambda v:v['per_share'] if v else None)(run(dict(a,ke=ke,terminal_growth=g))['valuation']) for g in [1.,1.5,2.,2.5,3.,3.5]]))
    out.update(scenarios=scenarios(),sensitivity=sensitivity(a),grid=grid,reverse=reverse_dcf(a),comps=comps())
    return out
