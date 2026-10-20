"""ELV financial, failure and package checks; python3 -m unittest -v."""
from copy import deepcopy
import importlib.util
import json
import unittest
import model as m

class ELVTests(unittest.TestCase):
    def test_synthetic_known_answer(self):
        # Five annual $100 distributions at 10%, g=0, followed by $100 perpetuity = $1000.
        v=m.equity_dcf([100.]*5,.10,0.,100.,10.)
        self.assertAlmostEqual(v['equity'],1000.)
        self.assertAlmostEqual(v['per_share'],100.)
    def test_original_elv_lab10_independent_regression(self):
        spec=importlib.util.spec_from_file_location('original',m.ROOT/'research/original_elv_lab10.py')
        old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
        r=m.run();rows=old.project();v=old.value(rows)
        self.assertAlmostEqual(v['per_share'],365.23895395950603)
        self.assertAlmostEqual(r['valuation']['per_share'],v['per_share'])
        for x,y in zip(r['rows'],rows):
            for k,val in y.items():self.assertAlmostEqual(x[k],val,msg=k)
    def test_filing_and_opening_mappings(self):
        self.assertTrue(all(c['pass'] for c in m.checks_base()))
        self.assertEqual(sum(m.ASSETS.values()),121494.)
        self.assertEqual(sum(m.LIABS.values()),77468.)
        self.assertEqual(m.HIST['shares'],220723898/1e6)
        self.assertEqual(m.HIST['cf_da'],1546.)
        self.assertEqual(m.HIST['depreciation']+m.HIST['software_amort'],979.)
        original=m.engine.OPENING['claims']
        try:
            m.engine.OPENING['claims']+=1
            with self.assertRaises(ValueError):m.run()
        finally:m.engine.OPENING['claims']=original
    def test_all_scenarios_articulate_and_roll_forward(self):
        for name,result in m.scenarios().items():
            self.assertTrue(result['valid'],(name,result['checks']))
            prior=m.engine.OPENING
            for r in result['rows']:
                self.assertAlmostEqual(r['opening_cash'],prior['cash'])
                self.assertAlmostEqual(r['equity'],prior['equity']+r['net_income']-r['buyback']-r['dividend'])
                self.assertAlmostEqual(r['claims_change'],r['claims']-prior['claims'])
                prior=r
    def test_predeclared_margin_change(self):
        a=m.run();b=m.run(dict(m.BASE,margin_shift=.5))
        self.assertEqual([k for k in m.BASE if a['inputs'][k]!=b['inputs'][k]],['margin_shift'])
        for key in ['ebit','fcfe']:self.assertGreater(b['rows'][-1][key],a['rows'][-1][key])
        self.assertAlmostEqual(b['valuation']['per_share'],378.818002947429)
        self.assertGreater(b['valuation']['per_share'],a['valuation']['per_share'])
    def test_cost_of_equity_and_growth(self):
        a=m.run();b=m.run(dict(m.BASE,ke=11.));c=m.run(dict(m.BASE,terminal_growth=3.))
        self.assertEqual(a['rows'],b['rows']);self.assertLess(b['valuation']['per_share'],a['valuation']['per_share'])
        self.assertGreater(c['valuation']['per_share'],a['valuation']['per_share'])
        for ke,g,shares in [(.1,.1,1),(.1,.11,1),(.1,.025,0)]:
            with self.assertRaises(ValueError):m.equity_dcf([100]*5,ke,g,100,shares)
    def test_equity_interest_not_financing_neutral(self):
        a=m.run();b=m.run(dict(m.BASE,debt_rate=m.BASE['debt_rate']+1.))
        self.assertEqual(a['rows'][0]['ebit'],b['rows'][0]['ebit'])
        for key in ['net_income','fcfe','cash']:self.assertLess(b['rows'][0][key],a['rows'][0][key])
        self.assertLess(b['valuation']['per_share'],a['valuation']['per_share'])
    def test_claims_timing_is_cash_not_profit(self):
        a=m.run();b=m.run(dict(m.BASE,claims_days=m.BASE['claims_days']+1))
        self.assertEqual(a['rows'][0]['ebit'],b['rows'][0]['ebit'])
        self.assertGreater(b['rows'][0]['claims'],a['rows'][0]['claims'])
        self.assertGreater(b['rows'][0]['fcfe'],a['rows'][0]['fcfe'])
    def test_failure_diagnostics_and_reset(self):
        baseline=m.run()
        for fault in ['cash','terminal']:
            bad=m.run(fault=fault);self.assertFalse(bad['valid']);self.assertIsNone(bad['valuation'])
            self.assertNotIn('sensitivity',m.dashboard(fault=fault))
        bad=m.run(fault='cash');gaps={c['name']:c['gap'] for c in bad['checks']}
        self.assertAlmostEqual(gaps['2026 balance sheet'],-100.)
        self.assertAlmostEqual(gaps['2026 cash flow ties to cash'],-100.)
        self.assertEqual(m.run(),baseline)
    def test_liquidity_failure_not_hidden(self):
        bad=m.run(dict(m.BASE,buyback=6000.,margin_shift=-1.,expense_shift=2.))
        self.assertFalse(bad['valid']);self.assertIsNone(bad['valuation'])
        self.assertTrue(any('liquidity' in c['name'] and not c['pass'] for c in bad['checks']))
    def test_signed_negative_cashflows_preserved(self):
        a=m.equity_dcf([-100,100,100,100,100],.1,.025,102.5,10)
        b=m.equity_dcf([0,100,100,100,100],.1,.025,102.5,10)
        self.assertAlmostEqual(b['equity']-a['equity'],100/1.1)
    def test_terminal_bridge_no_double_debt_subtraction(self):
        r=m.run();v=r['valuation'];last=r['rows'][-1]
        self.assertAlmostEqual(v['terminal_cash'],(last['fcfe']+last['repayment'])*1.025)
        self.assertAlmostEqual(v['equity'],v['pv_flows']+v['pv_terminal'])
        self.assertAlmostEqual(v['per_share'],v['equity']/m.HIST['shares'])
    def test_bad_controls_refused(self):
        for bad in [None,True,float('nan'),float('inf'),999,'3']:
            with self.assertRaises(ValueError):m.run(dict(m.BASE,growth=bad))
        with self.assertRaises(ValueError):m.run(dict(m.BASE,company='ABG'))
        with self.assertRaises(ValueError):m.run({})
    def test_sensitivity_independence_and_invalid_endpoints(self):
        before=deepcopy(m.BASE);items=m.sensitivity(m.BASE)
        self.assertEqual(m.BASE,before);self.assertEqual(len(items),len(m.DRIVERS)*2)
        for x in items:
            for side in ['low','high']:
                actual=m.run(dict(m.BASE,**{x['driver']:x[side+'_input']}))
                self.assertEqual(x[side]['value'],actual['valuation']['per_share'] if actual['valuation'] else None)
            if not x['valid']:self.assertIsNone(x['value_span'])
    def test_peers_definitions_and_reverse_solver(self):
        c=m.comps();self.assertEqual([x['ticker'] for x in c['rows']],['ELV','UNH','CI'])
        self.assertAlmostEqual(c['pe_range'][0],280.91/22.18*25.21)
        self.assertAlmostEqual(c['pe_range'][1],388.28/13.23*25.21)
        r=m.reverse_dcf(m.BASE);self.assertTrue(r['solved']);self.assertAlmostEqual(r['value'],350.55,places=6)
        self.assertFalse(m.reverse_dcf(m.BASE,price=10000)['solved'])
    def test_active_company_and_json(self):
        d=m.dashboard();self.assertEqual(d['meta']['ticker'],'ELV')
        json.dumps(d,allow_nan=False)
        page=(m.ROOT/'index.html').read_text()
        for unwanted in ['ABG','Asbury','New vehicles','Floor-plan','FCFF span','WACC / g']:
            self.assertNotIn(unwanted,page)
        self.assertIn('ELV_selected_run_',page)

if __name__=='__main__':unittest.main()
