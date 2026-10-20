# Lab 09 — Pro-Forma Build: Elevance Health

**David Zarate · Elevance Health, Inc. (NYSE: ELV)**  
**Prepared: September 24, 2026 · Model origin: December 31, 2025 · Forecast: FY2026–FY2030**

The five-year ELV model produces an illustrative common-equity value of **$80,516.64 million**, or **$364.78 per opening share**. **74.93%** of that value comes from cash flows after 2030. Each forecast balance sheet balances, cash stays above the modeled minimum, and the cash-flow statement reconciles to the change in cash.

This is a historical-base classroom forecast using FY2025 filings and explicit judgments. It is not a September 2026 fair-value estimate or an updated forecast incorporating interim 2026 results. The supplied lab requires the ABG known answer, so the same Python file also runs ABG and reproduces **$291.75** exactly to the cent. ABG is now the default company; select ELV with `--company ELV`.

## D — Define the question

> What are five years of a company's statements worth, built from assumptions you can defend, and how do you know the statements are right?

My answer is conditional: they are worth the discounted equity cash flows that the operating, investment and financing assumptions can support. A balanced model proves accounting consistency; it does not prove that growth, margins or distributable cash are realistic.

The three operating judgments are:

1. **Revenue growth:** 3% annually for ELV. This assumes modest expansion, with no separate acquisition program. It deliberately does not extrapolate a single strong historical growth year indefinitely.
2. **Blended gross margin:** 14.3%, 14.5%, 14.7%, 14.8%, 14.8%. This means revenue less benefit expense and product costs. It assumes gradual pricing and medical-cost improvement, then stabilization. It is a model subtotal, not ELV's reported medical loss ratio.
3. **Cash operating expense / gross profit:** 71.2%, 70.8%, 70.4%, 70.0%, 70.0%. This assumes modest operating efficiency. Depreciation is removed from the historical operating-expense anchor before it is modeled separately.

The corresponding ABG judgments are the handout's 1.8% revenue growth, 17.05% gross margin and SG&A/gross-profit path of 66.5%, 65.5%, 64.5%, 64.5%, 64.5%.

## R — Represent the opening position and assumptions

All dollar amounts below are **USD millions**; shares are in millions. Historical inputs are from the [ELV FY2025 Form 10-K, balance sheet p. 71, income statement p. 72, cash flows p. 74, and Debt Note 13](https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/elv-20251231.htm). Ratios are calculated without rounding in the code.

### Historical input ledger

| Input | FY2025 value / aggregation |
|---|---:|
| Operating revenue | 197,584 |
| Benefit expense; product costs | 148,223; 21,178 |
| Operating expense | 20,984 |
| D&A; intangible amortization | 1,546; 628 |
| Investment income; equity-method earnings | 2,194; 398 |
| Interest expense; capex | 1,402; 1,116 |
| Repurchases; dividends | 2,605; 1,529 |
| Cash | 9,491 |
| Receivables | 10,073 + 5,162 + 6,307 = 21,542 |
| PP&E | 4,679 |
| Investments | 25,884 + 740 + 1,121 + 10,839 = 38,584 |
| Intangibles | 11,200 |
| Other assets | 28,344 goodwill + 5,344 current + 2,310 noncurrent = 35,998 |
| **Assets** | **121,494** |
| Claims payable | 17,084 |
| Debt | 150 + 1,099 + 30,797 = 32,046 |
| Other liabilities | 77,468 − 17,084 − 32,046 = 28,338 |
| Revolver drawn | 0 |
| Common equity; noncontrolling interests | 43,882; 144 |
| **Liabilities + equity** | **121,494** |
| Shares outstanding | 220.723898 |

Source: [FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/elv-20251231.htm). The opening check is **121,494 − 77,468 − 43,882 − 144 = 0**.

### Forecast rules

Historical anchors do not make the forecasts facts. Every decision to carry a ratio or dollar amount forward is a modeling judgment.

| Assumption | Forecast rule | Classification and defense |
|---|---|---|
| Growth, margin and expense efficiency | Three paths above | Judgment; modest growth and gradual recovery |
| PP&E-related D&A | Opening PP&E × (1,546 − 628) / 4,679 | Historical proxy, held constant; includes PP&E-related amortization rather than claiming pure depreciation |
| Intangible amortization | 628 annually | History-anchored judgment; reduce intangible assets separately |
| Impairment | 0 | Judgment; no speculative future write-down |
| Capex | 1,116 annually | History-anchored judgment; no acquisition spending |
| Tax | 24% of positive pretax income; zero tax benefit on losses | Normalized judgment |
| Receivables | Revenue × 21,542 / 197,584 | Historical ratio, held constant |
| Claims payable | Direct costs × 17,084 / (148,223 + 21,178) | Historical fixed-mix proxy; claims are operating liabilities, not loans |
| Other working-capital investment | Change in revenue × 5,344 / 197,584 | Other current assets grow with revenue; goodwill and other noncurrent assets stay flat |
| Investment assets | Flat at 38,584 | Simplification; no portfolio purchases, gains or losses |
| Normalized investment income | 2,194 − 398 = 1,796 annually | Judgment: exclude equity-method earnings and treat the remainder as cash income |
| Debt interest | Opening debt × 1,402 / 32,046 | Historical expense/balance proxy, approximately 4.375%; not a market borrowing quote |
| Net debt repayment | 1,000 annually | Judgment; assumes maturities above this amount are refinanced |
| Buybacks; dividends | 2,605; 1,529 annually | Hold historical dollars; neither is subtracted from FCFE used in valuation |
| Minimum cash | 9,491 | Judgment: preserve opening consolidated cash, not a regulatory minimum |
| Revolver limit; interest | 5,000; 6% | Historical facility capacity; assumed interest rate |
| Other liabilities; NCI | Flat; future NCI income/distributions zero | Simplification; model net income is assigned to common equity |
| Cost of equity; terminal growth | 10%; 2.5% | Judgments using the lab's discounting convention |
| Valuation denominator | 220.723898 opening shares | Opening common shares, not an EPS weighted average |

The [credit facility disclosure](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001156039/6858e352-f3fd-432c-9300-518ba85cd10d.pdf) establishes $5,000 million of capacity and a September 2030 maturity. Availability through the entire forecast assumes renewal; the base case does not draw it. The model does not test the facility's contractual covenants.

The historical blended margin is 14.2638%, and operating expense excluding the D&A proxy divided by gross profit is 71.1989%. These calculations explain the starting forecast choices; they do not establish that the subsequent improvements will occur.

## I — Implement the three statements

[proforma.py](proforma.py) is a single file using only Python's standard library. It calculates revenue, gross profit, cash operating expenses, depreciation, amortization, investment income, interest, tax and net income. Interest uses opening debt and revolver balances, avoiding a circular cash/interest calculation.

Next it projects every noncash balance-sheet line. Receivables and other current assets use revenue drivers; claims payable uses a direct-cost driver. PP&E increases with capex and falls with depreciation. Intangibles fall with amortization. Common equity increases with net income and falls with dividends and buybacks.

For ELV:

```text
CFO = net income + depreciation + amortization
      − increase in receivables − increase in other working capital
      + increase in claims payable
FCFE = CFO − capex − scheduled net debt repayment
Cash before revolver = opening cash + FCFE − buybacks − dividends
```

A shortfall draws only available revolver capacity. A surplus first repays any opening revolver. If maximum borrowing cannot meet minimum cash, the model raises an error. Closing cash is the last computed balance-sheet line; it is not set to an arbitrary number to make the sheet balance.

ELV has no modeled dealership inventory or floor-plan loans. Any inventory within its other current assets is included in that aggregate working-capital driver. The cash-flow statement separates operating, investing and financing cash flows. In the ABG branch, floor-plan changes appear in operating cash flow and enter FCFE exactly as the lab requires.

### Run commands

```sh
python3 dcf.py                           # Prior lab: $537.84
python3 proforma.py --company ELV        # ELV: three statements, checks, valuation
python3 proforma.py --company ABG        # Required training case
python3 proforma.py --check              # Known answer and failure tests
python3 proforma.py --company ABG --break-cash  # Intentional error; nonzero exit
```

Use `python` instead of `python3` if that is the Python 3 command on your computer. Full generated statements and verification output are saved in [lab09-output.md](lab09-output.md).

## V — Verify the model

### ELV forecast summary

| Line (USD millions) | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Operating revenue | 203,511.5 | 209,616.9 | 215,905.4 | 222,382.5 | 229,054.0 |
| Operating income, after D&A | 6,835.4 | 7,290.3 | 7,778.4 | 8,232.6 | 8,508.7 |
| Net income | 5,494.4 | 5,873.3 | 6,277.5 | 6,656.0 | 6,899.0 |
| Cash from operations | 6,738.9 | 7,112.8 | 7,536.6 | 7,950.5 | 8,225.8 |
| FCFE | 4,622.9 | 4,996.8 | 5,420.6 | 5,834.5 | 6,109.8 |
| Closing cash | 9,979.9 | 10,842.7 | 12,129.3 | 13,829.8 | 15,805.6 |
| Debt | 31,046.0 | 30,046.0 | 29,046.0 | 28,046.0 | 27,046.0 |
| Balance-sheet gap | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

Every year passes assets minus liabilities minus total equity, cash minimum, revolver capacity and cash-flow reconciliation checks. `assert_balanced` recalculates the balance-sheet total from its components and raises an error naming the year and gap. The valuation calls this function before discounting any cash flows.

### Required ABG proof

| Line | FY2026E | FY2030E |
|---|---:|---:|
| Revenue | 18,323.0 | 19,678.3 |
| Operating income | 844.2 | 971.4 |
| Net income | 413.6 | 527.5 |
| FCFE | 211.4 | 342.3 |
| Closing cash | 101.8 | 719.8 |
| Assets − liabilities − equity | 0.0 | 0.0 |

ABG equity value is **$5,237.34 million**, value per share is **$291.75**, and the post-2030 share is **79.76%**. All ten displayed endpoint operating figures and the per-share answer match the handout. Checks use full precision; printed statements use one decimal.

Replacing FY2026 cash with the opening 40.4 causes:

```text
ValueError: FY2026E: assets - liabilities - equity gap = -61.4
```

The model refuses to value the damaged statements. The automated test changes a copy, preserving the valid case. Additional tests exercise a revolver draw, subsequent repayment, a funding shortfall beyond available capacity, and terminal growth equal to the discount rate.

## Value the equity

Following the lab's exact convention:

```text
Equity value = sum(FCFE_t / 1.10^t), t = 1,...,5
             + [(FCFE_2030 + repayment_2030) × 1.025 / (0.10 − 0.025)] / 1.10^5
```

| ELV valuation component | Value |
|---|---:|
| PV of 2026–2030 FCFE | 20,183.53 |
| Normalized 2031 FCFE | 7,287.53 |
| Terminal value at FY2030 end | 97,167.07 |
| PV of terminal value | 60,333.10 |
| **Common-equity value** | **80,516.64** |
| **Post-2030 contribution** | **74.93%** |
| **Value per opening share** | **$364.78** |

The terminal formula adds back the final year's repayment because it assumes net debt paydown stops after 2030. Debt is refinanced thereafter; it is not assumed to disappear. This is the handout's terminal shortcut, not a complete steady-state capital structure model. The terminal cash flow is extrapolated rather than obtained from a sixth projected balance sheet.

FCFE already reflects interest, tax and debt repayment. Accordingly, I use cost of equity and do not subtract debt again. I do not add consolidated cash or investment assets as excess cash. Distributions reduce the balance sheet's cash and equity; subtracting them again from the valued FCFE would double count the payout decision. Opening shares divide the aggregate equity value; the model does not forecast an EPS denominator or assume a buyback execution price.

The earlier $537.84 DCF remains unchanged. Its model origin, forecast dates, FCFF cash-flow assumptions, WACC and cash/debt bridge differ. Its price and this $364.78 exercise are not directly comparable estimates at one valuation date.

## Floor-plan explanation

Floor-plan loans finance a dealer's vehicle inventory through manufacturers' finance arms or banks. In the ABG exercise, they rise with inventory; interest is charged on the opening loan balance. New borrowing offsets inventory's cash use in the lab's FCFE calculation.

The scale explains the video's roughly negative $1.1 billion cash outcome. In this model, ABG's FY2026 closing floor-plan balance is **2,063.9**. If that funding is withdrawn and the opening loans must be repaid, then even using the entire 850 revolver gives **101.8 − 2,063.9 + 850 = −1,112.0** of cash. This is a counterfactual funding shortfall, not an accepted forecast. Merely hiding a row would instead break the accounting. ELV's medical claims liability reflects unpaid insurance obligations and is not floor-plan borrowing.

## Reflect and interpret

**Why compute cash last?** Cash is the accumulated result of operations, reinvestment, debt movements and shareholder distributions. Computing it last allows the independently calculated balance-sheet check to expose missing transactions or inconsistent assumptions. Setting cash directly to force a balance would defeat the test.

**What does −61.4 tell me before opening a cell?** Assets are 61.4 below liabilities plus equity. The specified cash replacement removed exactly that year's generated cash. The magnitude and sign identify the missing increase in cash; it is a model error, not a negative enterprise value.

**What does the ELV result depend on?** The recovery in blended margins and expense efficiency creates growing earnings and FCFE. Nearly three quarters of value still depends on post-2030 cash flows. Flat investment assets, no new acquisitions, flat other liabilities, cash taxes equal to tax expense, no OCI and no separate stock-compensation add-back keep the exercise simple. Operating expenses other than D&A are treated as cash; there is no separate future equity issuance or dilution schedule.

The largest economic limitation is insurer capital: consolidated cash and claims reserves do not establish how much a regulated subsidiary can distribute to the parent. Preserving 9,491 of cash is only a liquidity assumption. A decision-grade valuation would need statutory capital, subsidiary dividend capacity, portfolio reinvestment, reserve development and parent cash/debt schedules. Balanced statements alone do not resolve those issues.

## Checkout

Files prepared for individual submission:

- [lab-09-elv.md](lab-09-elv.md): assumptions, sources, method, results and reflections.
- [proforma.py](proforma.py): runnable ELV engine, ABG benchmark and checks.
- [lab09-output.md](lab09-output.md): complete generated statements and test evidence.

The prior DCF was rerun successfully. The partner discussion and human file swap remain personal classroom activities; the automated break test does not claim that they occurred. This folder has no Git repository configured, so these files have not been uploaded and no GitHub submission links have been invented. Upload them to the course/work repository and submit their actual GitHub file links.
