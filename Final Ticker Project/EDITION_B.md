# Project 1 — Edition B

**David Zarate · Elevance Health, Inc. (NYSE: ELV) · October 19, 2026**

*AI-assisted draft for my review, synthesized from my saved labs, research records, and final workbench. Historical figures below describe those saved analyses; this document does not update market data or certify an original AI-off checkpoint.*

## Final decision and intended user

My recommendation remains **watch / defer**. The intended user is a buy-side investment committee deciding whether to initiate an ELV position when the fund currently owns none. The final workbench produces a conditional equity valuation range of **$267.48–$495.07 per opening common share**, with a **$365.24 base case**. These scenarios make the recovery assumptions explicit, but they do not establish a current trading opportunity. Before recommending initiation, I would need stronger evidence of medical-cost recovery, sustainable cash conversion, and cash that regulated subsidiaries can actually distribute to the parent.

The final model uses a **December 31, 2025 valuation origin**, FY2025 historical statements, and a **2026–2030 forecast**. The FY2025 filing was published February 6, 2026, so this is a retrospective exercise using information published after the valuation origin. The peer comparison uses **September 10, 2026 prices**. Neither is an October 19 price target. The forecast horizon is five years; the accompanying model guide proposes a 12–24 month monitoring discussion, subject to the committee confirming its actual mandate.

Statement amounts are in USD millions. The valuation denominator is **220.723898 million opening common shares**, rather than annual weighted-average diluted shares. Buybacks reduce projected cash and equity, but the model does not forecast their execution price or a changing share count. Full numerical results are available without running Python in the [saved model report](outputs/BASE_REPORT.md).

## How the evidence changed my analysis

My early research identified a tension between ELV's scale, cash generation, and healthcare-services businesses and its medical-cost, membership, and margin pressures. The [September research report](research/edition_b_sources/Elevance_Health_2026-09-03_report.md) and [Lab 4 screen](research/edition_b_sources/LAB%204.md) supported watch/defer. Insider purchases and repurchases were reasons to investigate, but they did not establish intrinsic value. The September report is titled Edition A and discloses AI assistance; I use it here as saved research history, without claiming that it is the required unchanged AI-off checkpoint.

The labs gradually replaced a broad recovery thesis with assumptions that could be calculated and challenged:

| Stage | Saved result or change | Implication for my judgment |
|---|---|---|
| Lab 5: initial cash-flow valuation | First-pass FCFF DCF of **$375.44**; its historical $400.66 reference price implied about **7.15%** annual FCFF growth under the selected assumptions. | A valuation needs an explicit recovery path and required return. The price alone cannot tell me whether recovery is adequately supported. |
| Lab 6: sensitivity and reverse DCF | Base **$537.84**; discount-rate/growth sensitivity corners **$346.14–$1,036.00**. | The range exposed substantial dependence on terminal assumptions. A higher base estimate did not demonstrate that the company had become more valuable. |
| Labs 7–8: comparable-company policy | Lab 7 practiced peer selection with ABG. The ELV application in Lab 8 produced **$319.28–$739.87**, with a **$529.58** median. | Business mix and earnings definitions determine whether a peer multiple is informative. Removing one peer materially changes the result. |
| Lab 9: linked statements | ELV pro-forma value **$364.78**. Medical claims payable became an explicit operating cash-flow driver. | Revenue, costs, working capital, financing, and cash must connect before I interpret value. |
| Lab 10: filing-based refinement | The PP&E D&A input changed from a **$918 million** residual proxy to the **$979 million** Note 9 measure; value became **$365.24**. | Source definitions can change the forecast even when the broad thesis is unchanged. The remaining D&A reconciliation difference must stay visible. |
| Lab 11: operating sensitivity | Revenue growth generated the larger operating-profit span; margin generated the larger FCFE and value spans over the tested ranges. | The driver that matters most depends on the output, the tested interval, and the cash-flow mechanism. |
| Final workbench | Bounded controls, linked statements, alternative sensitivity ranges, visible checks, reset, and saved output. | A teammate can challenge the assumptions and trace the consequences without editing the accounting engine. |

Sources: [Lab 5](research/edition_b_sources/Lab%205.md), [Lab 6](research/lab-06-elv.md), [Lab 7](research/edition_b_sources/lab-07-elv.md), [Lab 8](research/lab-08-elv.md), [Lab 9](research/edition_b_sources/lab-09-elv.md), [Lab 10](research/lab-10-elv.md), and [Lab 11](research/Lab11_elv-operating-sensitivity.md).

The earlier **$537.84** estimate and final **$365.24** estimate use different dates, forecasts, discount rates, and valuation structures. Their difference is not a measured decline in ELV's intrinsic value. The first is an enterprise FCFF exercise; the final model values a consolidated FCFE proxy directly. My [Lab 12 discussion record](research/edition_b_sources/Lab12_discussion.md) highlighted that disagreement. Its comparisons with a September market price are illustrative; they do not turn the historical-origin pro forma into a same-date valuation.

## What the final model assumes

ELV's company-specific operating liability is **medical claims payable**. It represents unpaid insurance claims and changes operating cash flow. It is not interest-bearing debt. Higher revenue also requires receivables and other working-capital assets, so growth in earnings does not translate dollar-for-dollar into cash available to shareholders.

The base case assumes 3% annual revenue growth, blended gross margin increasing from 14.3% to 14.8%, and cash operating expense declining from 71.2% to 70.0% of blended gross profit. Blended gross margin is a calculated measure after benefit expense and product costs; it is **not ELV's medical benefit ratio**. The following are forecast judgments, even where historical figures anchor them.

| Load-bearing assumption | Base and basis | Challenge and evidence that would change it |
|---|---|---|
| Revenue growth | **3% annually**, carried from Lab 10. | A single growth rate combines membership, pricing, and services. Revise it using membership, premium yields, rate adequacy, and Carelon external revenue. |
| Blended margin | **14.3% → 14.8%**, compared with the calculated FY2025 level of about 14.26%. | Recovery may be too optimistic if utilization and product costs outpace pricing. Revise the path using medical-cost trends, payer mix, and service economics. |
| Cash expense / gross profit | **71.2% → 70.0%**, anchored to the historical expense proxy. | Technology, staffing, and compliance costs may absorb efficiency gains. Require evidence that savings are sustainable. |
| Claims payment timing | **42.07 days**, based on year-end claims payable divided by annual benefit expense. | A year-end ratio does not establish reserve adequacy. Review settlement patterns, reserve development, and statutory filings. |
| Capital expenditure | **$1,116 million annually**, held at FY2025 spending. | Flat spending may underfund maintenance and growth. Review software investment and capital commitments. |
| Normalized tax / investment income | **24% tax**; **$1,796 million investment income**, after removing $398 million of equity-method earnings from reported investment income. | Book and cash taxes can differ; remaining investment income is assumed to be cash. Reconcile these assumptions to tax and portfolio evidence. |
| Cost of equity / terminal growth | **10% / 2.5%**, retained from the lab model. | These are selected assumptions. Reassess required return and the capital needed to support perpetual growth. |

The full [assumption-challenge record](records/ASSUMPTION_CHALLENGE.md) also covers debt costs, repayment, buybacks, and locked simplifications. Scheduled net debt repayment is $1,000 million annually during the forecast. The terminal calculation assumes this net repayment stops after 2030 and remaining debt is refinanced. Investment assets stay flat, and there is no separate statutory-capital growth schedule.

The D&A refinement improved the connection to the asset schedule, but it did not resolve every definition issue: $979 million of selected PP&E D&A plus $628 million of other intangible amortization totals $1,607 million, compared with the reported $1,546 million cash-flow D&A adjustment. The [model guide](MODEL_GUIDE.md) discloses that difference rather than forcing a reconciliation.

## Valuation, sensitivity, and disagreement across methods

The final model calculates **FCFE proxy = operating cash flow − capital expenditure − scheduled net debt repayment**, before dividends, buybacks, and liquidity-only revolver movements. It discounts signed cash flows at cost of equity. Debt is not subtracted a second time, and consolidated cash and investments are not added as freely distributable surplus assets.

| Final scenario | Value per opening share | FY2030 operating profit, $m | FY2030 FCFE, $m | Economic explanation |
|---|---:|---:|---:|---|
| Low | **$267.48** | 7,244.14 | 5,228.12 | Slower growth, cost pressure, weaker efficiency, and a higher required return. |
| Base | **$365.24** | 8,479.57 | 6,116.77 | Modest growth and gradual margin and expense recovery. |
| High | **$495.07** | 9,527.42 | 6,779.37 | Stronger growth, improved margins and efficiency, and a lower required return. |

These are conditional scenarios, not confidence bounds. **74.91% of base equity value comes from post-2030 cash flows**, making terminal economics central to the conclusion. The reverse DCF implies a **10.2974% cost of equity** at the saved December 31, 2025 close of $350.55, holding base operations and terminal growth fixed. This is a retrospective conditional calculation, not an independent estimate of the market's required return. See the [saved report](outputs/BASE_REPORT.md).

Lab 11 tested annual revenue growth from **2% to 4%** and shifted every annual blended margin by **−0.50 to +0.50 percentage points**. Revenue growth produced a **$987.56 million** FY2030 operating-profit span, versus **$687.16 million** for margin. Margin produced the larger FCFE span, **$515.51 million** versus **$501.38 million**, and the larger value span, **$27.16** versus **$22.31** per share.

The mechanism explains the ranking: higher growth generates profit but also requires additional receivables and other working capital. A margin improvement increases profit without increasing revenue-based receivables, although lower benefit costs reduce claims funding. For example, a **+0.50 percentage-point margin shift** raises FY2030 operating profit by **$343.58 million**, FCFE by **$257.76 million**, and value from **$365.24 to $378.82**. These are saved executed results, not my original AI-off prediction. The final app additionally tests alternative ranges because ranking over one interval does not prove universal driver importance.

The P/E comparison qualifies UnitedHealth and Cigna as peers, using September 10, 2026 prices and FY2025 reported GAAP diluted EPS. Their implied ELV values span **$319.28–$739.87**. Removing UnitedHealth leaves **$319.28**, showing how dependent the midpoint is on peer choice. Business mix and unusual reported earnings further limit comparability. I would not average this reference range with the equity DCF: their dates and economic assumptions differ. The [peer policy](research/PEER_POLICY.md) explains the qualifications.

## Validation and the role of AI

AI helped assemble research, write and revise Python, generate explanations, and build the interface. The useful standard is whether a claim can be traced to evidence and whether a model can expose a failure. A fluent explanation or a passing calculation does not settle the investment judgment.

The saved [validation record](records/AI_USE_AND_VALIDATION.md) documents historical filing mappings, the opening balance sheet, and the cash reconciliation, including the foreign-exchange effect. Automated checks cover linked statements, valuation directionality and boundaries, peer definitions, and failure recovery. The project retains a [cold-run log](records/COLD_RUN.log) and [submission-check log](records/SUBMISSION_CHECKS.log). Those records document technical execution; they do not establish that all course requirements are complete.

The product makes an accounting failure visible: removing **$100 million** of FY2026 cash without a corresponding transaction creates balance-sheet and cash-flow gaps of **−$100 million**, and valuation is withheld. Reset restores the valid base. Funding-capacity failures and invalid terminal assumptions also prevent an apparently usable valuation from being displayed.

Two AI/model corrections are particularly relevant. First, the prior final package used a different company; after I identified the mismatch, the active package was rebuilt around ELV. Second, the final equity DCF retains negative interim FCFE and its funding cost rather than omitting negative flows under the older lab convention. The positive base case is unchanged by that correction. These examples show why I need to review both the task being implemented and the financial logic.

Validation still has limits. The final synthetic valuation test is not claimed to reproduce the instructor's official training-case answer. AI-assisted source checks are not independent human reviews. My saved Lab 11 records do not contain the authentic locked human prediction or completed partner challenge record. Lab 12 records a group discussion, but does not establish those missing pre-run steps. This Edition B does not invent a prediction, timestamp, partner quotation, or receipt.

## Conditions for changing the decision

I would reconsider initiation when operating evidence supports the recovery assumptions, parent liquidity and subsidiary distribution capacity support the projected cash flows, and a refreshed valuation offers sufficient compensation for downside at a same-date market price. The committee memo proposes a **20% discount to a reviewed valuation** as a working discipline. That is an analyst proposal, not a supplied client mandate or a signal derived from an October quote.

I would weaken or reject the investment thesis if medical-cost pressure persists despite repricing, reserve development undermines reported earnings, or capital and refinancing needs materially reduce distributable cash. A required **0.50 percentage-point reduction in the blended margin path** is a practical model review trigger; Lab 11 shows its value effect. The percentage is a proposed monitoring threshold, not an empirically proven failure boundary.

My later [Lab 13 mandate exercise](research/edition_b_sources/lab-13-response.md) reinforces a useful distinction: a portfolio can pass mechanical allocation checks without demonstrating that it meets the client's objective. The same distinction applies here. Balanced statements establish internal consistency; they do not establish adequate shareholder returns or insurer capital capacity. I do not import that separate exercise's client rules into the ELV committee mandate.

The main development in my analysis is therefore the evidence behind watch/defer. Early work identified a potentially attractive recovery. The final workbench makes the cost of that recovery visible through margins, working capital, cash flow, financing, and terminal assumptions. My recommendation remains conditional because important parts of that recovery and distributable-capital case still need evidence.

## Submission boundary

The preserved [Project 1 assignment](research/ASSIGNMENT.md) excludes insurers and requires FCFF/WACC, an enterprise-to-equity bridge, and an enterprise multiple. This ELV workbench uses FCFE/cost of equity and P/E. Its economic rationale does not establish instructor approval; the departure remains unresolved in the [submission checklist](SUBMISSION_CHECKLIST.md).

This Edition B is a new AI-assisted synthesis. The unchanged original Edition A and its receipt, genuine human validation records, and exact Edition B format still need to be matched to the official shared checklist. My three videos have been prepared, as reported for this draft; their contents, corrected transcripts, and grader access have not been verified here.
