"""ELV linked statements, adapted from the existing Lab 10. USD millions.
Valuation and workbench checks live in model.py.
"""
from copy import deepcopy
import math

SOURCES = {
    2023: "https://www.sec.gov/Archives/edgar/data/1156039/000115603924000015/elv-20231231.htm",
    2024: "https://s202.q4cdn.com/665319960/files/doc_financials/2025/ar/Elevance-Health-2024-10K-color.pdf",
    2025: "https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/elv-20251231.htm",
}
# Each year's own 10-K: consolidated balance sheet, income and cash flows; Note 9.
# None means not separately disclosed/confirmed; it never means zero inventory.
HISTORY = {
    2023: dict(revenue=170209., prior_revenue=155660., benefits=124330., products=17293.,
               opex=20087., net_income=5991., common_income=5987., inventory=None,
               ppe=4359., equity=39306., dep=107., software_amort=765.,
               cf_da=1745., intangible_amort=885., capex=1296., tax=1724.,
               pretax=7715., claims=16111., cfo=8061.),
    2024: dict(revenue=175204., prior_revenue=170209., benefits=127567., products=19750.,
               opex=20025., net_income=5971., common_income=5980., inventory=None,
               ppe=4652., equity=41315., dep=105., software_amort=809.,
               cf_da=1393., intangible_amort=580., capex=1256., tax=1933.,
               pretax=7904., claims=15746., cfo=5808.),
    2025: dict(revenue=197584., prior_revenue=175204., benefits=148223., products=21178.,
               opex=20984., net_income=5661., common_income=5662., inventory=None,
               ppe=4679., equity=43882., dep=94., software_amort=885.,
               cf_da=1546., intangible_amort=628., capex=1116., tax=1049.,
               pretax=6710., claims=17084., cfo=4290.),
}
OPENING = dict(year=2025, revenue=197584., cash=9491., receivables=21542.,
               ppe=4679., investments=38584., intangibles=11200., other_assets=35998.,
               claims=17084., debt=32046., revolver=0., other_liabilities=28338.,
               equity=43882., nci=144.)
# Carrying historical ratios into future years is a judgment, not guidance.
ASSUMPTIONS = dict(
    growth=[.03]*5, margin=[.143, .145, .147, .148, .148],
    cash_opex_ratio=[.712, .708, .704, .700, .700],
    ppe_da_ratio=(94+885)/4679, intangible_amort=628., capex=1116., tax=.24,
    benefit_share=148223/(148223+21178), claims_to_benefits=17084/148223,
    receivables_ratio=21542/197584, other_wc_ratio=5344/197584,
    investment_income=2194-398, debt_rate=1402/32046, net_repayment=1000.,
    buyback=2605., dividend=1529., minimum_cash=9491.,
    revolver_limit=5000., revolver_rate=.06, ke=.10, terminal_growth=.025,
    shares=220.723898,
)
TOL = 1e-6


def totals(r):
    assets = sum(r[k] for k in ("cash", "receivables", "ppe", "investments", "intangibles", "other_assets"))
    liabilities = sum(r[k] for k in ("claims", "debt", "revolver", "other_liabilities"))
    return assets, liabilities, assets-liabilities-r["equity"]-r["nci"]


def check(rows, a):
    """Recompute checks from components; raise rather than force a balance."""
    for r in rows:
        year = r["year"]
        if any(not math.isfinite(v) for v in r.values() if isinstance(v, (int, float))):
            raise ValueError(f"FY{year}: non-finite output")
        gap = totals(r)[2]
        if abs(gap) > TOL:
            raise ValueError(f"FY{year}: assets - liabilities - equity gap = {gap:.1f}")
        if r["cash"] < a["minimum_cash"]-TOL:
            raise ValueError(f"FY{year}: cash below floor by {a['minimum_cash']-r['cash']:.1f}")
        if not -TOL <= r["revolver"] <= a["revolver_limit"]+TOL:
            raise ValueError(f"FY{year}: revolver outside capacity")
        if min(r[k] for k in ("debt", "ppe", "intangibles")) < -TOL:
            raise ValueError(f"FY{year}: negative debt or long-lived asset")
        if "cfo" in r:
            cash_gap = r["cash"]-r["opening_cash"]-r["cfo"]-r["cfi"]-r["cff"]
            if abs(cash_gap) > TOL:
                raise ValueError(f"FY{year}: cash-flow reconciliation gap = {cash_gap:.1f}")


def project(a=ASSUMPTIONS, *, validate=True):
    p = dict(OPENING)
    if validate:
        check([p], a)
    rows = []
    for i, year in enumerate(range(2026, 2031)):
        r = dict(p, year=year)
        r["revenue"] = p["revenue"]*(1+a["growth"][i])
        r["gross_profit"] = r["revenue"]*a["margin"][i]
        r["direct_costs"] = r["revenue"]-r["gross_profit"]
        r["benefits"] = r["direct_costs"]*a["benefit_share"]
        r["products"] = r["direct_costs"]-r["benefits"]
        r["cash_opex"] = r["gross_profit"]*a["cash_opex_ratio"][i]
        r["ppe_da"] = p["ppe"]*a["ppe_da_ratio"]
        r["amort"] = a["intangible_amort"]
        r["operating_income"] = r["gross_profit"]-r["cash_opex"]-r["ppe_da"]-r["amort"]
        r["investment_income"] = a["investment_income"]
        r["interest"] = p["debt"]*a["debt_rate"]+p["revolver"]*a["revolver_rate"]
        r["pretax"] = r["operating_income"]+r["investment_income"]-r["interest"]
        r["tax"] = max(0., r["pretax"])*a["tax"]
        r["net_income"] = r["pretax"]-r["tax"]
        r["receivables"] = r["revenue"]*a["receivables_ratio"]
        r["claims"] = r["benefits"]*a["claims_to_benefits"]
        r["other_wc_change"] = (r["revenue"]-p["revenue"])*a["other_wc_ratio"]
        r["other_assets"] = p["other_assets"]+r["other_wc_change"]
        r["capex"] = a["capex"]
        r["ppe"] = p["ppe"]+r["capex"]-r["ppe_da"]
        r["intangibles"] = p["intangibles"]-r["amort"]
        r["repayment"] = min(a["net_repayment"], p["debt"])
        r["debt"] = p["debt"]-r["repayment"]
        r["buyback"], r["dividend"] = a["buyback"], a["dividend"]
        r["equity"] = p["equity"]+r["net_income"]-r["buyback"]-r["dividend"]
        # Investment assets, other liabilities and NCI flat; no future OCI or NCI income.
        r["receivables_change"] = r["receivables"]-p["receivables"]
        r["claims_change"] = r["claims"]-p["claims"]
        r["cfo"] = (r["net_income"]+r["ppe_da"]+r["amort"]-r["receivables_change"]
                    -r["other_wc_change"]+r["claims_change"])
        r["cfi"] = -r["capex"]
        r["fcfe"] = r["cfo"]+r["cfi"]-r["repayment"]
        r["opening_cash"] = p["cash"]
        available = p["cash"]+r["fcfe"]-r["buyback"]-r["dividend"]
        if available < a["minimum_cash"]:
            r["revolver_change"] = min(a["minimum_cash"]-available, a["revolver_limit"]-p["revolver"])
        else:
            r["revolver_change"] = -min(available-a["minimum_cash"], p["revolver"])
        r["revolver"] = p["revolver"]+r["revolver_change"]
        r["cff"] = -r["repayment"]-r["buyback"]-r["dividend"]+r["revolver_change"]
        r["cash_change"] = r["cfo"]+r["cfi"]+r["cff"]
        r["cash"] = p["cash"]+r["cash_change"]
        if validate:
            check([r], a)
        rows.append(r)
        p = r
    return rows

