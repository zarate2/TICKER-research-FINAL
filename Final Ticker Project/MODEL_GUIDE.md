# Model guide — Elevance Health (ELV)

## Decision, security and dates

The intended user is a buy-side analyst team advising a portfolio manager with no ELV position. The proposed action is **watch / defer**, subject to medical-cost recovery, cash conversion and regulated capital evidence. The model projects FY2026–2030 and supports a 12–24 month monitoring discussion.

Security: Elevance Health, Inc., NYSE: ELV common stock. Currency: USD. Statements are millions; prices are dollars per share. Equity value is divided by **220.723898 million December 31, 2025 common shares**. These are opening shares, not weighted-average diluted EPS shares. Repurchases change projected cash and equity but do not create a separately forecast share count or EPS series.

The valuation origin is **2025-12-31** and its historical close is **$350.55**. The base-year 10-K was published **2026-02-06**, so the model uses later evidence and is not a backtest available at year-end. The P/E reference retains the saved Lab 08 **2026-09-10** price date; it is not a same-date independent confirmation of DCF. Rebuilt and source checks performed 2026-10-19. No live market recommendation is supplied.

## ELV economics and model structure

Health benefits, pharmacy and services drive ELV. The company-specific balance-sheet line is **medical claims payable**: an operating obligation tied to benefit expense. Investment assets, normalized investment income and the cash/parent funding problem also matter. This model extends the saved Lab 10 rather than substituting another company’s operating drivers.

`elv_forecast.py` computes the linked statements. `model.py` maps bounded controls into annual assumptions, reconciles filing inputs, rejects invalid results, values FCFE, and computes sensitivities/peers. `app.py` serves the locked engine to index.html. `build_report.py` uses the same functions for saved output. All use Python’s standard library.

## Historical inputs and reconciliation

The main source is [ELV FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/elv-20251231.htm), printed pp. 71–74. `research/HISTORICAL_INPUTS.json` records individual filing asset/liability rows, opening model mappings and normalization decisions. `research/SOURCES.json` gives dates and locators. Prior 2023–2024 history is retained from Lab 10 and labeled as not reverified in this rebuild.

| FY2025 input | USD millions |
|---|---:|
| Operating revenue | 197,584 |
| Benefit expense | 148,223 |
| Product costs | 21,178 |
| Operating expense | 20,984 |
| Investment income | 2,194 |
| Interest expense | 1,402 |
| Net income / income to common | 5,661 / 5,662 |
| Total assets / total liabilities | 121,494 / 77,468 |
| Common equity / NCI | 43,882 / 144 |
| Cash / medical claims payable | 9,491 / 17,084 |
| CFO / investing cash flow / financing cash flow | 4,290 / −1,344 / −1,738 |

The historical cash reconciliation includes −5 of FX: 8,288 + 4,290 − 1,344 − 1,738 − 5 = 9,491. Receivables aggregate 10,073 + 5,162 + 6,307 = 21,542. Debt aggregates 150 + 1,099 + 30,797 = 32,046. Investments aggregate 25,884 + 740 + 1,121 + 10,839 = 38,584. Other liabilities aggregate directly from filing rows, never from a forecast balancing gap.

## Normalization catalog: facts versus judgments

| Item | Treatment and unresolved risk |
|---|---|
| Blended gross margin | Calculated as (operating revenue − benefits − product costs) / operating revenue. FY2025 14.2638%. ELV does not report this as a consolidated gross-margin metric; it is not 1 minus medical benefit ratio. |
| Expense proxy | Subtract selected PP&E D&A of 979 from reported operating expense; resulting cash-expense proxy / blended gross profit is 71.1989%. Other noncash expenses are not separately modeled. |
| PP&E D&A | Prior Lab 10 uses Note 9 depreciation 94 plus software/leasehold amortization 885 =979, divided by opening PP&E 4679. Add separate intangible amortization 628. Their sum 1607 differs from reported CFO D&A 1546; this scope difference remains unresolved, not forced into a plug. |
| Investment income | Normalize 2194 −398 equity-method earnings =1796 and assume the remainder is cash. Flat portfolio and this cash classification are simplifying judgments. |
| Financial-instrument losses | Reported 653 is reconciled historically but not projected. This is a forward assumption, not proof those losses cannot recur. |
| Taxes | Use 24% normalized tax, replacing FY2025 1049/6710 =15.63%. Cash taxes equal modeled book taxes; no automatic tax asset on losses. |
| Legal/other items | No blanket one-time addback. Historical operating expense is the anchor; the future ratio path is a judgment, not a fully audited adjusted-earnings reconciliation. |
| Insurer capital | No consolidated cash or investments are added as surplus value. The cash floor does not establish statutory capital or cash distributable to the parent. |

## Forecast controls and locked assumptions

The base uses 3% revenue growth each year; blended margins 14.3%, 14.5%, 14.7%, 14.8%, 14.8%; and cash expense / gross profit 71.2%, 70.8%, 70.4%, 70.0%, 70.0%. Margin and expense controls shift every annual value by the same number of percentage points. A +0.50 pp shift changes the margin path to 14.8%, 15.0%, 15.2%, 15.3%, 15.3%.

Benefit expense gets the historical 148223/(148223+21178) share of direct costs; the rest is product costs. Claims payable = benefit expense × claims days /365. The base claims timing is 42.069449 days. Receivables / revenue is 21542/197584; incremental other working capital / incremental revenue is 5344/197584. These ratios are judgments when carried into forecasts.

Capex is 1116 annually; intangible amortization 628; investment assets 38584 stay flat. Opening-debt interest uses 1402/32046; revolver interest is 6% of opening revolver. Scheduled net debt paydown is 1000 annually; other maturities are assumed refinanced. Cash floor is 9491; facility capacity 5000 assumes September 2030 renewal, without a covenant model. Buybacks 2605 and dividends 1529 hold historical dollars. Other liabilities and NCI remain flat; future NCI earnings/distributions, OCI, acquisitions and separate stock compensation/issuance are zero. Those simplifications need review.

Each exposed driver has value, bounds, basis, challenge and revision evidence in `records/ASSUMPTION_CHALLENGE.md` and the app. Bounds are analyst stress ranges, not management guidance. The record also identifies fixed choices that need challenge.

## Statement articulation

```text
Revenue = prior revenue × (1 + growth)
Blended gross profit = revenue × blended margin
Operating income = gross profit − cash expense − PP&E D&A − intangible amortization
Net income = operating income + investment income − interest − tax
CFO = net income + PP&E D&A + intangible amortization
      − increase in receivables − increase in other working-capital assets
      + increase in medical claims payable
CFI = −capex
FCFE proxy = CFO − capex − scheduled net debt repayment
CFF = −scheduled repayment − buybacks − dividends + revolver movement
Closing cash = opening cash + CFO + CFI + CFF
Common equity = opening equity + net income − buybacks − dividends
```

PP&E and intangibles follow separate roll-forwards. Cash is calculated from flows, never chosen to balance assets. Revolver draws cover a cash-floor shortfall only up to capacity; surplus repays outstanding revolver before accumulating cash. Interest uses opening balances to avoid circularity. Insufficient capacity fails visibly and withholds value.

## Equity valuation and terminal assumption

Discount the five **signed** FCFE proxy values at cost of equity (base 10%). Negative interim values retain their funding cost, correcting the earlier lab’s positive-only convention. The base is unchanged because all its flows are positive.

```text
Terminal FCFE = (2030 FCFE + 2030 scheduled net repayment) × (1 + g)
Terminal value = terminal FCFE / (cost of equity − g)
Equity value = PV(five annual FCFE values) + PV(terminal value)
Value/opening share = equity value / 220.723898
```

This is a direct equity valuation; subtracting debt again or adding the consolidated investment portfolio would double count or misclassify value. Distributions are not subtracted again from pre-distribution FCFE. Liquidity-only revolver proceeds are excluded from valued FCFE; a draw flags the model for review because facility repayment and parent capital capacity are simplified.

The terminal formula assumes net scheduled paydown stops after 2030 and remaining debt is refinanced. It extrapolates cash flow without a sixth-year balance sheet or statutory-capital reinvestment model. Base equity value is **80,616.97**, value/opening share **$365.24**, and post-2030 contribution **74.91%**. These are conditional outputs, not validated distributable capital.

## Cases, sensitivity and market expectations

Low/base/high values are **$267.48 / $365.24 / $495.07**. Cases jointly change growth, margins, efficiency, capex and discount/terminal assumptions; exact dictionaries and causal descriptions are in model.py and BASE_RUN.json.

One-at-a-time analysis recalculates every linked statement at both endpoints with all other independent controls fixed. It ranks FY2030 operating profit, FCFE and value separately, then repeats at narrower local intervals. Invalid accounting/funding endpoints are withheld from every ranking. Claims timing changes cash without operating profit; more claims funding is not evidence of better insurance economics.

The reverse DCF solves for cost of equity within 8–12%, holding operations and terminal growth fixed. At **$350.55** on the historical origin date, the base implies **10.2974%**. This is conditional, uses the later filing, and is not an independently estimated market required return.

## Comparable-company policy

ELV is the target. UNH and CI are qualified health-benefits/services peers; their 2026-09-10 closes are 388.28 and 280.91 and FY2025 GAAP diluted EPS 13.23 and 22.18. ELV uses close 416.54 and EPS 25.21 on the same reference basis. Every P/E is price / annual reported diluted EPS; implied ELV price is peer P/E ×25.21, with no debt adjustment.

The range is **$319.28–$739.87**. Excluding UNH leaves **$319.28**; excluding CI leaves **$739.87**. Earnings quality, government-program mix and the separate reference date explain why this range need not match DCF. Do not average them. No transaction multiple is included without a defensible control/synergy/time basis. See research/PEER_POLICY.md.

## Failure checks and course boundary

Historical filing totals and opening mappings reconcile before projection. Each year tests the balance sheet, cash-flow identity, FCFE cash bridge, finite outputs, nonnegative asset/debt balances and liquidity capacity. Accounting tolerance is 1e-6 USD million. Injecting −100 of FY2026 cash fails two identities and withholds valuation. Invalid inputs or a nonpositive terminal cash flow are rejected.

The automated suite covers a synthetic known answer, the existing ELV Lab 10 regression, directionality, claims timing, equity interest sensitivity, signed funding needs, failure recovery, peer definitions and reverse solving. The synthetic test is not claimed as an official training-case answer supplied by the instructor.

The supplied Project 1 assignment excludes insurers and requires enterprise FCFF/WACC and an EV multiple. This requested ELV build uses the prior insurer equity architecture and cannot claim those requirements are fulfilled. Preserve the original assignment text; obtain and record the instructor’s disposition in the checklist. No student precommit, original checkpoint, partner exchange or recording is fabricated.
