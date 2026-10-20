# Lab 10 — Pro-Forma: Elevance Health

**David Zarate · Elevance Health, Inc. (NYSE: ELV)**  
**Prepared September 24, 2026 · Opening balance sheet December 31, 2025 · Forecast FY2026–FY2030**

The five-year model implies **$80,616.97 million of common-equity value, or $365.24 per opening share**. All five forecast balance sheets balance, cash-flow statements reconcile, and cash stays above the modeled floor without drawing the revolver. **74.91% of value comes from cash flows after 2030.**

This is an AI-assisted classroom draft for student review. The filing research, calculations and runnable model are complete. The two personal filing checks and actual partner exchange remain pending; the prepared discussion below does not claim those activities occurred. The first-person assumption defenses are proposed wording to review and put in my own words before submission.

## Reopen and rerun

The existing `proforma.py` still runs the ABG case by default. Its known answer remains **$291.75 per share**, and its endpoint and failure checks pass. Lab 09 files are preserved. Lab 10 runs separately:

```sh
python3 proforma.py
python3 proforma.py --check
python3 lab10_proforma_elv.py
python3 lab10_proforma_elv.py --check
python3 lab10_proforma_elv.py --sensitivity
python3 lab10_proforma_elv.py --operating-sensitivity
python3 lab10_proforma_elv.py --break-cash
```

The last command deliberately exits with an error. Use `python` instead if that is the installed Python 3 command. The new file uses only the standard library and does not import the Lab 09 engine.

The operating-sensitivity command uses the agreed revenue-growth and blended-margin ranges, writes the [comparison and V/E evidence](Lab11_elv-operating-sensitivity.md), and retains [full inputs and annual statement details](Lab11_elv-operating-sensitivity-details.json). It finishes with a fresh base rerun. [Personal prediction and partner records](Lab11_elv-sensitivity-personal-record.md) remain separate and are not overwritten by reruns.

## D — Define the question and the company-specific line

> What are five years of your company's statements worth, built from assumptions you can defend?

**Company:** Elevance Health, Inc., ticker **ELV**.

**The line that makes ELV different:** Medical claims payable represents unpaid insurance claims, so I forecast it from benefit expense and put its annual change in operating cash flow; it is an operating liability, not a floor-plan loan or interest-bearing debt.

The model distinguishes benefit expense from product costs. It has no dealership inventory or floor-plan borrowing. Investment assets and normalized investment income remain visible because the insurer holds an investment portfolio. Regulatory capital and subsidiary dividend capacity are material limitations of this simplified consolidated model.

## R — Three years of filing history

All amounts are **USD millions** unless stated otherwise. Income and cash-flow figures cover the full fiscal year; balance-sheet figures are at December 31. Each year's main source is that year's own 10-K, with later comparative statements checked for consistency where available.

- **K23:** [FY2023 Form 10-K][K23], filed February 21, 2024. Balance sheet p. 69; income statement p. 70; cash flows p. 72; PP&E Note 9 p. 103; MD&A operating results.
- **K24:** [FY2024 Form 10-K, company-hosted copy][K24], filed February 20, 2025. Balance sheet p. 70; income statement p. 71; cash flows p. 73; PP&E Note 9 pp. 105–106; MD&A pp. 49 and 52–55. These are printed page numbers, not PDF viewer numbers.
- **K25:** [FY2025 Form 10-K][K25], filed February 6, 2026. Balance sheet p. 71; income statement p. 72; cash flows p. 74; PP&E Note 9 p. 107; MD&A operating results.

### Required history grid

| Item and definition | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Operating revenue, income statement | [170,209][K23] | [175,204][K24] | [197,584][K25] |
| Benefit expense, income statement | [124,330][K23] | [127,567][K24] | [148,223][K25] |
| Cost of products sold, income statement | [17,293][K23] | [19,750][K24] | [21,178][K25] |
| Blended gross profit, calculated: revenue − benefit expense − product costs | [28,586][K23] | [27,887][K24] | [28,183][K25] |
| SG&A proxy: reported operating expense, income statement | [20,087][K23] | [20,025][K24] | [20,984][K25] |
| Consolidated net income, income statement | [5,991][K23] | [5,971][K24] | [5,661][K25] |
| Shareholders' net income, after NCI | [5,987][K23] | [5,980][K24] | [5,662][K25] |
| Inventory, standalone balance | [Unresolved; not separately presented][K23] | [Unresolved; not separately presented][K24] | [Unresolved; not separately presented][K25] |
| PP&E, net, balance sheet | [4,359][K23] | [4,652][K24] | [4,679][K25] |
| Shareholders' equity, excluding NCI, balance sheet | [39,306][K23] | [41,315][K24] | [43,882][K25] |
| Medical claims payable, balance sheet | [16,111][K23] | [15,746][K24] | [17,084][K25] |

ELV does not report a consolidated line titled gross profit or SG&A. The two substitutions above are explicit modeling definitions. Blended gross margin is not one minus the medical benefit ratio: the latter uses premium revenue, while this model uses total operating revenue. Unconfirmed inventory is not entered as a historical zero; any inventory embedded in other current assets remains in that aggregate forecast, preventing double counting.

### Supporting history and ratios

| Filing input | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Depreciation alone, Note 9 | [107][K23] | [105][K24] | [94][K25] |
| Software and leasehold amortization, Note 9 | [765][K23] | [809][K24] | [885][K25] |
| PP&E D&A, sum of preceding two rows | [872][K23] | [914][K24] | [979][K25] |
| Total D&A cash-flow adjustment, as reported | [1,745][K23] | [1,393][K24] | [1,546][K25] |
| Other intangible amortization, income statement | [885][K23] | [580][K24] | [628][K25] |
| Pretax income, income statement | [7,715][K23] | [7,904][K24] | [6,710][K25] |
| Income tax expense, income statement | [1,724][K23] | [1,933][K24] | [1,049][K25] |
| Cash from operations, cash-flow statement | [8,061][K23] | [5,808][K24] | [4,290][K25] |

Ratios below are calculated from the cited inputs, using full precision in the Python file. PP&E denominators are year-end net balances, consistently across history; applying that ratio to a future opening balance is a forecast judgment.

| Ratio and formula | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Blended gross margin = blended gross profit / operating revenue | 16.79% | 15.92% | 14.26% |
| SG&A proxy / gross profit = reported operating expense / blended gross profit | 70.27% | 71.81% | 74.46% |
| Cash operating expense proxy / gross profit = (operating expense − Note 9 PP&E D&A) / gross profit | 67.22% | 68.53% | 70.98% |
| Inventory days = inventory / relevant inventory cost × 365 | Unresolved / not modeled separately | Unresolved / not modeled separately | Unresolved / not modeled separately |
| Depreciation alone / net PP&E | 2.45% | 2.26% | 2.01% |
| PP&E D&A including software / net PP&E | 20.00% | 19.65% | 20.92% |
| Effective tax rate = tax expense / pretax income | 22.35% | 24.46% | 15.63% |
| Reported operating revenue growth, calculated | 9.35% | 2.93% | 12.77% |
| Claims payment timing proxy = year-end medical claims payable / benefit expense × 365 | 47.30 days | 45.05 days | 42.07 days |

The claims-days measure is a simple year-end proxy, not the company's actuarial reserve-development measure. Growth for 2023 uses 2022 operating revenue of **155,660**, reported in K23's income statement. The MD&A rounds reported growth to 9.3%, 2.9% and 12.8%.

**Why the D&A refinement matters:** Lab 09 estimated PP&E-related D&A as 1,546 − 628 = 918. Lab 10 uses the more directly relevant Note 9 figure, 94 + 885 = **979**, and applies 979 / 4,679 to opening PP&E. The cash-flow adjustment and the sum of Note 9 PP&E D&A plus other intangible amortization are different reported measures; their classification/reconciliation difference is unresolved here. They are shown separately, not forced to tie or added together. Forecast D&A follows the explicitly selected asset schedule. Cash operating expenses are an approximation: other noncash items are not separately normalized.

### Capital spending: filing beside provider

| Period | Filing: purchases of property and equipment, cash outflow | Stock Analysis: Capital Expenditures | Model spending magnitude |
|---|---:|---:|---:|
| FY2023 | [(1,296)][K23] | [(1,296)][PROVIDER] | 1,296 |
| FY2024 | [(1,256)][K24] | [(1,256)][PROVIDER] | 1,256 |
| FY2025 | [(1,116)][K25] | [(1,116)][PROVIDER] | 1,116 |

The provider's annual field agrees with the filing after preserving the outflow sign. Acquisitions and purchases of investment securities are separate investing lines and are not folded into PP&E capex. Provider consulted September 24, 2026; filings control the model inputs.

### Reported growth beside organic growth

| Period | Reported operating revenue growth | Organic / same-store disclosure in reviewed MD&A |
|---|---:|---|
| FY2023 | [9.3%][K23] | Higher premium pricing is a cited driver; no comparable consolidated organic growth percentage identified. |
| FY2024 | [2.9%][K24] | Pricing, CarelonRx product revenue and acquisitions helped; Medicaid attrition offset growth. No comparable consolidated organic percentage identified. |
| FY2025 | [12.8%][K25] | Premium pricing, acquisitions and Medicare Advantage growth helped; Medicaid attrition offset growth. No comparable consolidated organic percentage identified. |

**Organic growth** is growth in the existing business after excluding acquisition/divestiture effects and any other adjustments specified by the company. ELV discusses organic expansion but does not provide a consolidated, quantified organic bridge in the reviewed MD&A passages. “Same-store” is a dealer/retail comparison, not an ELV operating metric. The missing organic percentage is unresolved; reported growth and membership growth are not substitutes for it.

**Why the video uses 1.8% for ABG when reported growth was 4.7%:** The assignment's distinction is between growth of stores already owned and total growth that also reflects changes in the business perimeter. Carrying the 1.8% existing-store rate forward avoids assuming that acquisition-driven sales repeat without acquisition spending. The two ABG percentages come from the Lab 10 prompt; they are not ELV inputs or a newly verified ABG filing reconciliation.

### Two personal filing checks — pending

The AI checked the source figures. The lab separately requires me to open the filings and check two items myself:

- [ ] **FY2025 operating revenue 197,584:** K25, printed p. 72, Consolidated Statements of Income. Confirm 164,639 premiums + 24,470 product revenue + 8,475 service fees = 197,584.
- [ ] **FY2025 medical claims payable 17,084:** K25, printed p. 71, Consolidated Balance Sheets. Confirm this is a liability and not a debt balance.

Personal verification date and notes: **pending student completion**.

### Opening balance sheet used by the engine

Every value is **history**, from [K25, printed p. 71][K25]. Aggregations preserve the full consolidated balance sheet.

| Asset | Amount | Liability or equity | Amount |
|---|---:|---|---:|
| Cash | 9,491 | Medical claims payable | 17,084 |
| Receivables: 10,073 + 5,162 + 6,307 | 21,542 | Debt: 150 + 1,099 + 30,797 | 32,046 |
| PP&E | 4,679 | Revolver drawn | 0 |
| Investments: 25,884 + 740 + 1,121 + 10,839 | 38,584 | Other liabilities: 77,468 − 17,084 − 32,046 | 28,338 |
| Other intangible assets | 11,200 | Common shareholders' equity | 43,882 |
| Other assets: 28,344 goodwill + 5,344 current + 2,310 noncurrent | 35,998 | Noncontrolling interests | 144 |
| **Total assets** | **121,494** | **Total liabilities and equity** | **121,494** |

Opening common shares are **220.723898 million**, also from that balance sheet. The equity check includes NCI; the valuation denominator is common shares, not a diluted earnings weighted-average denominator.

### Labeled assumption set

“History” describes an observed input. Applying its ratio or dollar amount to future years is labeled “judgment.” No forecast below is represented as company guidance. This is a retrospective FY2025-base exercise using subsequently published full-year statements, not a valuation that was actually knowable on December 31, 2025 or an interim-2026 update.

| Value | Label | Reason — proposed student defense |
|---|---|---|
| Opening balances and 220.723898 million common shares above | History | I start from the consolidated filing so every opening asset and liability has a source and the balance sheet reconciles. |
| Revenue growth: 3%, 3%, 3%, 3%, 3% | Judgment | I use modest expansion close to 2024's reported growth and do not assume another acquisition program. This is not a measured organic rate; pricing and membership could make the outcome materially different. |
| Blended gross margin: 14.3%, 14.5%, 14.7%, 14.8%, 14.8% | Judgment | I assume gradual pricing and claims-cost improvement from 14.26%, but stop below the 2023–2024 margins. Continued medical-cost pressure would invalidate that recovery. |
| Cash operating expense / gross profit: 71.2%, 70.8%, 70.4%, 70.0%, 70.0% | Judgment | I allow slight initial pressure against the revised 70.98% historical ratio, then modest efficiency gains. I do not assume a return to 2023's lower expense ratio. |
| Benefit share of direct costs: 148,223 / 169,401; product costs are the remainder | Judgment | I hold the 2025 mix constant to split total direct costs without inventing segment growth forecasts. A shift in insurance versus pharmacy business would require changing this assumption. |
| Claims payable / benefit expense: 17,084 / 148,223 = 11.5259%, about 42.07 days | Judgment | I retain the latest payment-timing proxy and let claims payable rise with benefits. I would change it for evidence of faster settlement, reserve development or different claims mix. |
| Separate floor-plan debt and interest: none | Judgment | ELV is not a vehicle dealer. I model medical claims as operating obligations and retain actual financial debt separately. |
| Separate inventory schedule: none; inventory amount unresolved | Judgment | I keep other current assets in an aggregate working-capital schedule rather than invent inventory days or add an unsupported inventory balance. |
| Receivables / revenue: 21,542 / 197,584 = 10.9027% | Judgment | I hold collection timing constant; the forecast still requires more receivables as revenue grows. |
| Other working-capital asset increase: revenue change × 5,344 / 197,584 = 2.7047% | Judgment | I scale other current assets with the business, while holding goodwill and other noncurrent assets flat. |
| PP&E D&A: opening net PP&E × 979 / 4,679 = 20.9233% | Judgment | Software is a large part of ELV's PP&E, so depreciation alone would miss much of the asset consumption. I use the direct Note 9 measure and one opening-balance rate to avoid circularity. |
| Other intangible amortization: 628 annually | Judgment | I use the latest annual expense as a simple run rate and reduce the intangible asset balance by the same amount; this is not the filing's future amortization schedule. |
| Capex: 1,116 annually | Judgment | I hold the latest spending level while assuming no acquisition program. This is below the prior two years, and inflation or technology investment could require a higher amount. |
| Tax: 24% of positive pretax income; no loss tax benefit | Judgment | I use a normalized rate close to 2024's 24.46% rather than extending 2025's 15.63% indefinitely. I do not recognize loss-related tax benefits without evidence they can be used. |
| Investments: 38,584, flat; normalized investment income: 2,194 − 398 = 1,796 annually | Judgment | I exclude equity-method earnings from the income run rate and assume the remainder is cash income. I hold the portfolio flat instead of forecasting security returns and purchases without a separate investment model. |
| Debt interest: opening debt × 1,402 / 32,046 = 4.3750% | Judgment | I use the latest expense-to-ending-balance proxy, not a current borrowing quote. Refinancing at different rates would change it. |
| Net debt repayment: 1,000 annually | Judgment | I assume gradual deleveraging and refinancing of maturities above this net amount; I am not claiming contractual maturities are only 1,000 each year. |
| Buybacks 2,605 and dividends 1,529 annually | Judgment | I keep historical cash distributions constant for liquidity testing. They reduce cash and equity but are not subtracted twice from the FCFE valuation. |
| Minimum consolidated cash: 9,491 | Judgment | I preserve opening liquidity as a simple floor. This is not a statutory capital requirement or proof that subsidiary cash can be distributed. |
| Revolver capacity 5,000; opening draw zero | History | K25 Debt Note 13 reports the facility and no opening balance drawn. |
| Revolver interest 6%; facility available throughout forecast | Judgment | I use an illustrative rate and assume renewal beyond its September 2030 maturity. Base-case value does not rely on drawing it; covenants are not modeled. |
| Other liabilities 28,338 and NCI 144 remain flat; future NCI income/distributions zero | Judgment | I keep residual balances fixed to focus this exercise on claims, receivables and reinvestment; forecast net income is assigned to common equity. |
| Acquisitions, disposals, impairments, OCI and separate share issuance: zero | Judgment | I do not add transactions or gains that I cannot forecast. Stock compensation is not separately added back, and there is no future EPS share-count or buyback-price schedule. |
| Cash taxes equal forecast tax expense; other operating costs treated as cash | Judgment | I avoid inventing deferred-tax and noncash schedules. This makes forecast CFO a normalized model output rather than a reconstruction of reported CFO. |
| Cost of equity 10%; perpetual growth 2.5% | Judgment | I require a double-digit equity return and keep long-run growth below the explicit 3% revenue assumption. These are classroom hurdles, not a current CAPM estimate; sensitivity shows their impact. |
| Terminal net debt paydown stops; final FCFE is normalized by adding back repayment | Judgment | I retain the Lab 09 convention that debt is refinanced after 2030. Debt remains outstanding, and this shortcut is not a fully projected steady-state balance sheet. |

**Prepared partner challenge, not an actual exchange:** “Why use a 24% tax rate when the most recent filing shows only 15.63%, and what would make you change it?”

**Prepared answer — two sentences:** I use 24% because it is close to 2024's 24.46% effective rate and does not assume that 2025's unusually low rate persists. I would lower it if later filings show recurring tax benefits and a sustainable lower effective rate, rather than simply one favorable year.

## I — ELV through the engine

[lab10_proforma_elv.py](lab10_proforma_elv.py) contains the three-year input ledger, opening balance sheet, assumptions, forecasts, valuation, sensitivity and failure checks. Cash is computed last from transactions; it is not typed to force a balance.

```text
Revenue = prior revenue × (1 + growth)
Gross profit = revenue × blended margin
Direct costs = revenue − gross profit
Benefit expense = direct costs × fixed benefit share
Claims payable = benefit expense × claims-to-benefits ratio

Net income = (gross profit − cash operating expense − PP&E D&A
              − intangible amortization + investment income − interest) − tax

CFO = net income + PP&E D&A + intangible amortization
      − increase in receivables − increase in other working-capital assets
      + increase in medical claims payable
CFI = − capex
FCFE = CFO − capex − net scheduled debt repayment
CFF = − net scheduled debt repayment − buybacks − dividends + revolver change
Closing cash = opening cash + CFO + CFI + CFF
Closing common equity = opening common equity + net income − buybacks − dividends
```

Interest uses opening debt and revolver balances. A cash shortfall draws only available revolver capacity; subsequent surplus repays the revolver before accumulating excess cash. A shortfall beyond borrowing capacity raises an error. PP&E and intangibles roll forward with their related investment and amortization.

The medical-claims driver is equivalent to Lab 09's combined-cost proxy while the benefit/product mix is fixed, but now its insurance-specific link is explicit. Cash-flow classification is consistent: changes in claims payable enter CFO; debt and revolver movements enter financing cash flow.

## V — Statements, checks and valuation

The following are the complete ELV forecast statements. All amounts are USD millions, and every forecast year is an estimate. The separately runnable output is saved in [lab10-output.md](lab10-output.md).

### Income statement

| USD millions | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Operating revenue | 203,511.5 | 209,616.9 | 215,905.4 | 222,382.5 | 229,054.0 |
| Benefit expense | -152,605.2 | -156,816.6 | -161,143.2 | -165,783.0 | -170,756.5 |
| Product costs | -21,804.1 | -22,405.8 | -23,024.0 | -23,687.0 | -24,397.6 |
| Blended gross profit | 29,102.1 | 30,394.4 | 31,738.1 | 32,912.6 | 33,900.0 |
| Cash operating expense | -20,720.7 | -21,519.3 | -22,343.6 | -23,038.8 | -23,730.0 |
| PP&E depreciation and amortization | -979.0 | -1,007.7 | -1,030.3 | -1,048.3 | -1,062.4 |
| Other intangible amortization | -628.0 | -628.0 | -628.0 | -628.0 | -628.0 |
| Operating income after D&A | 6,774.4 | 7,239.5 | 7,736.1 | 8,197.5 | 8,479.6 |
| Normalized investment income | 1,796.0 | 1,796.0 | 1,796.0 | 1,796.0 | 1,796.0 |
| Interest | -1,402.0 | -1,358.3 | -1,314.5 | -1,270.8 | -1,227.0 |
| Pretax income | 7,168.4 | 7,677.3 | 8,217.6 | 8,722.8 | 9,048.6 |
| Tax expense | -1,720.4 | -1,842.5 | -1,972.2 | -2,093.5 | -2,171.7 |
| Net income to common | 5,448.0 | 5,834.7 | 6,245.4 | 6,629.3 | 6,876.9 |

### Balance sheet

| USD millions | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Cash | 9,994.5 | 10,869.5 | 12,166.2 | 13,875.2 | 15,858.0 |
| Receivables | 22,188.3 | 22,853.9 | 23,539.5 | 24,245.7 | 24,973.1 |
| PP&E | 4,816.0 | 4,924.3 | 5,010.0 | 5,077.7 | 5,131.3 |
| Investments | 38,584.0 | 38,584.0 | 38,584.0 | 38,584.0 | 38,584.0 |
| Intangibles | 10,572.0 | 9,944.0 | 9,316.0 | 8,688.0 | 8,060.0 |
| Other assets | 36,158.3 | 36,323.4 | 36,493.5 | 36,668.7 | 36,849.2 |
| TOTAL ASSETS | 122,313.1 | 123,499.2 | 125,109.3 | 127,139.4 | 129,455.5 |
| Medical claims payable | 17,589.1 | 18,074.5 | 18,573.2 | 19,107.9 | 19,681.2 |
| Debt | 31,046.0 | 30,046.0 | 29,046.0 | 28,046.0 | 27,046.0 |
| Revolver | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Other liabilities | 28,338.0 | 28,338.0 | 28,338.0 | 28,338.0 | 28,338.0 |
| TOTAL LIABILITIES | 76,973.1 | 76,458.5 | 75,957.2 | 75,491.9 | 75,065.2 |
| Common equity | 45,196.0 | 46,896.7 | 49,008.1 | 51,503.4 | 54,246.3 |
| Noncontrolling interests | 144.0 | 144.0 | 144.0 | 144.0 | 144.0 |
| LIABILITIES + EQUITY | 122,313.1 | 123,499.2 | 125,109.3 | 127,139.4 | 129,455.5 |

### Cash flow statement

| USD millions | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Net income | 5,448.0 | 5,834.7 | 6,245.4 | 6,629.3 | 6,876.9 |
| PP&E D&A | 979.0 | 1,007.7 | 1,030.3 | 1,048.3 | 1,062.4 |
| Intangible amortization | 628.0 | 628.0 | 628.0 | 628.0 | 628.0 |
| Increase in receivables | -646.3 | -665.6 | -685.6 | -706.2 | -727.4 |
| Increase in other working capital | -160.3 | -165.1 | -170.1 | -175.2 | -180.4 |
| Increase in medical claims payable | 505.1 | 485.4 | 498.7 | 534.8 | 573.2 |
| CASH FROM OPERATIONS | 6,753.5 | 7,125.0 | 7,546.7 | 7,959.0 | 8,232.8 |
| Capex / CASH FROM INVESTING | -1,116.0 | -1,116.0 | -1,116.0 | -1,116.0 | -1,116.0 |
| Net debt repayment | -1,000.0 | -1,000.0 | -1,000.0 | -1,000.0 | -1,000.0 |
| FCFE before distributions and revolver | 4,637.5 | 5,009.0 | 5,430.7 | 5,843.0 | 6,116.8 |
| Buybacks | -2,605.0 | -2,605.0 | -2,605.0 | -2,605.0 | -2,605.0 |
| Dividends | -1,529.0 | -1,529.0 | -1,529.0 | -1,529.0 | -1,529.0 |
| Revolver draw / (repayment) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| CASH FROM FINANCING | -5,134.0 | -5,134.0 | -5,134.0 | -5,134.0 | -5,134.0 |
| CHANGE IN CASH | 503.5 | 875.0 | 1,296.7 | 1,709.0 | 1,982.8 |
| Opening cash | 9,491.0 | 9,994.5 | 10,869.5 | 12,166.2 | 13,875.2 |
| Closing cash | 9,994.5 | 10,869.5 | 12,166.2 | 13,875.2 | 15,858.0 |

### Checks

| USD millions | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Assets - liabilities - equity | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cash-flow reconciliation gap | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cash above floor | 503.5 | 1,378.5 | 2,675.2 | 4,384.2 | 6,367.0 |
| Revolver drawn | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |


### What these ELV results mean

The forecast assumes that pricing and medical-cost management gradually improve the blended gross margin from 14.3% to 14.8%, while cash operating expense falls from 71.2% to 70.0% of gross profit. Revenue grows from **$203.51 billion in 2026 to $229.05 billion in 2030**, and net income increases from **$5.45 billion to $6.88 billion**. These are model outcomes, not company guidance.

The insurance-specific cash-flow link is visible in medical claims payable, which rises from **$17.08 billion at the opening date to $19.68 billion in 2030**. Its annual increase adds to CFO because those expenses have been recognized before cash payment; the liability remains an obligation to settle claims. It is not treated as interest-bearing debt or automatically distributable cash.

Annual FCFE increases from **$4.64 billion to $6.12 billion** after capex and scheduled net debt repayment. Over the forecast, debt falls by **$5.00 billion**, cash rises from **$9.49 billion to $15.86 billion**, and the revolver remains undrawn. The value of **$365.24 per opening share** still depends heavily on the terminal assumptions because **74.91%** comes from cash flows after 2030.

**No year draws the revolver:** operating cash generation covers capex, scheduled net debt repayment, distributions and the minimum cash requirement. Every year has positive net income and FCFE, so the lab's negative-FCFE branch is not needed. If final FCFE were negative, a growing perpetuity would not establish a defensible going-concern value without an explicit recovery forecast. The code refuses that terminal calculation; for negative interim FCFE it labels the year and follows the lab's positive-years-only convention, explicitly warning that omitting funding needs overstates economic value.

**Refusal proof:** replacing FY2026 closing cash with the opening 9,491 produces:

```text
ValueError: FY2026: assets - liabilities - equity gap = -503.5
```

The damaged statements are rejected before valuation. The automated checks also exercise temporary revolver borrowing and repayment, insufficient funding, and terminal growth equal to cost of equity. Tests use full precision, not the displayed rounding.

### One value per share

```text
Equity value = Σ FCFE_t / (1.10)^t, t = 1,...,5
             + [(FCFE_2030 + net repayment_2030) × 1.025 / (0.10 − 0.025)] / 1.10^5
```

| Component | USD millions unless stated |
|---|---:|
| PV of FY2026–FY2030 FCFE | 20,224.63 |
| Normalized FY2031 FCFE | 7,294.69 |
| Terminal value at FY2030 end | 97,262.47 |
| PV of terminal value | 60,392.34 |
| **Common-equity value** | **80,616.97** |
| Opening common shares, millions | 220.723898 |
| **Value per opening share** | **$365.24** |
| Post-2030 share of value | 74.91% |

FCFE already includes interest, taxes and scheduled debt repayment, so it is discounted at cost of equity. No second debt subtraction or consolidated cash/investment addition is made. Buybacks and dividends are distributions of the cash being valued, not another deduction from it. The model values current common equity using opening shares; it does not forecast diluted EPS or presume a buyback execution price.

The Lab 09 result was $364.78. Using Note 9's direct PP&E D&A rate changes the result to **$365.24**, approximately **$0.45 higher using unrounded values**. Higher noncash expense reduces earnings but modestly increases modeled after-tax cash flow through the assumed tax shield; PP&E also rolls forward differently. The original Lab 09 calculation is preserved for comparison.

### Sensitivity: dollars per opening share

| Cost of equity / terminal growth | 2.0% | 2.5% | 3.0% |
|---|---:|---:|---:|
| 9% | $399.49 | $424.59 | $453.88 |
| 10% | $346.89 | $365.24 | $386.21 |
| 11% | $306.08 | $319.96 | $335.58 |

These are parameter sensitivities holding operating forecasts constant, not a statistical confidence interval. The concentration in terminal value makes the long-run assumptions material.

### Market comparison: dated, same denominator

The same-day [Investing.com search snapshot][QUOTE] retrieved September 24, 2026 displayed **$396.98**, marked intraday, at provider time **14:24:20**; its time zone was not specified in the retrieved text. This is an observed same-day intraday snapshot, not a verified closing price or live quote. The opened historical page lagged at September 23, and another provider's search/open snapshots conflicted, so a September 24 official close remains **unresolved**. As a separately dated cross-check, [Stock Analysis][PRICE_HISTORY] showed September 23's close of **$398.56**.

**Required comparison question:** The historical-base model says **$365.24** and the September 24 intraday market snapshot says **$396.98** per share, equivalent to **$80,616.97 million versus $87,622.97 million on the same 220.723898 million opening shares**—what different growth, margins, required return or regulatory-capital needs would explain the gap?

The market equivalent above is price multiplied by the model's denominator, not ELV's actual current market capitalization. Holding the denominator constant does not align valuation dates: the DCF is discounted to year-end 2025 and omits interim 2026 information. This is a lab comparison and a research question, not a recommendation or a measured current mispricing.

## E — Fresh-eyes review

The prepared tax-rate attack and two-sentence defense appear directly under the assumption table. They are practice material, not evidence of an actual partner conversation.

**Specific question prepared to ask my partner:** “If your revenue forecast includes acquisition-driven growth, where have you included acquisition spending and its financing, and how much would your value per share fall if you used the organic rate instead?”

Actual exchange record to complete after discussion:

- Partner and date: **pending**.
- Their actual challenge to one judgment: **pending**.
- My two-sentence answer, revised if needed after discussion: **pending**.
- My actual challenge to their model and the assumption it addressed: **pending**.

## Reflect

**The judgment I would defend longest:** I would defend treating claims payable as an operating liability tied to benefit expense. It connects ELV's insurance obligations to the cash-flow statement and prevents the model from treating claims reserves as a discretionary funding source. The exact 42.07-day proxy is less certain than that classification and should change when payment timing or reserve evidence changes.

**The filing number that surprised me:** Operating revenue rose 12.8% in 2025, yet consolidated CFO fell from 5,808 to 4,290. The filing attributes the CFO decline to a settlement payment, working-capital effects and lower shareholders' income; this illustrates why revenue growth alone does not establish cash generation. [K25, MD&A liquidity][K25].

**What the balanced statements do not prove:** The cash floor is not statutory capital, and consolidated cash is not automatically distributable to common shareholders. Flat investment assets, flat residual liabilities, no acquisitions, constant capex, simplified taxes and an extrapolated terminal cash flow all limit the estimate. In particular, modeled CFO rebounds from 4,290 in 2025 to 6,753.5 in 2026; that is a normalization assumption, not a demonstrated cash recovery. A fuller insurer valuation would require subsidiary dividend capacity, reserve development, parent liquidity and a sustainable terminal reinvestment/capital schedule.

## Checkout

Files prepared:

- [lab-10-elv.md](lab-10-elv.md): history, sources, labels, defenses, valuation discussion and review prompts.
- [lab10_proforma_elv.py](lab10_proforma_elv.py): standalone ELV model and failure checks.
- [lab10-output.md](lab10-output.md): all three statements, checks, valuation, sensitivity and execution evidence.

Before submission, complete the two personal filing checks, put the defenses into my own words, and record the actual partner exchange. The workspace has no Git repository configured, so no upload has been performed and no GitHub links have been invented. Upload these three files to the course/work repository and submit their actual GitHub file links.

[K23]: https://www.sec.gov/Archives/edgar/data/1156039/000115603924000015/elv-20231231.htm
[K24]: https://s202.q4cdn.com/665319960/files/doc_financials/2025/ar/Elevance-Health-2024-10K-color.pdf
[K25]: https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/elv-20251231.htm
[PROVIDER]: https://stockanalysis.com/stocks/elv/financials/
[QUOTE]: https://www.investing.com/equities/wellpoint-inc-historical-data
[PRICE_HISTORY]: https://stockanalysis.com/stocks/elv/history/
