# Lab 08 — Deal Evidence and Valuation Triangulation

**David Zarate · Elevance Health, Inc. (NYSE: ELV)**  
**Valuation date: September 10, 2026 · Prepared: September 17, 2026**

The two qualified peers imply **$319.28–$739.87 per ELV share**, with **$529.58 at the peer median P/E**. The saved Week 3 DCF gives **$537.84**, with sensitivity corners of **$346.14–$1,036.00**. My proposed call remains **watch-defer**: the median and DCF are close, but the peer spread and earnings differences make that agreement weak evidence of fair value.

This AI-assisted draft follows [Session 8](../slides-session-08.md) and the [full Lab 08 assignment](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-04/lab-08-deal-triangulation.md). It extends [Lab 07](lab-07-elv.md) and preserves the saved [Lab 06 DCF](lab-06-elv.md). The policy and investment judgments below are proposed for student review. This document does not claim that the required before-AI writing, human partner discussion, or independent second-AI discussion occurred.

## 1. Reopen and explain

The existing calculator and DCF were rerun successfully:

```sh
python3 lab07_comps.py
python3 dcf.py
```

The Lab 07 Asbury case still produces its expected $215.81–$246.18 range and $231.00 median estimate. Those training inputs are not used to value ELV. The DCF reproduces $537.84 per diluted share, WACC of 6.986920%, terminal growth of 2.50%, and an 81.07% terminal-value contribution to enterprise value.

**Method explanation:** P/E is the price of one common share divided by annual diluted earnings attributable to that share. A peer's P/E becomes an ELV reference price by multiplying that multiple by ELV's annual diluted EPS. This compares prices relative to earnings across differently sized companies. It assumes sufficiently similar business risks and earnings prospects; a lower multiple can reflect weaker expected growth or less sustainable earnings. Since P/E is an equity multiple, no cash or debt adjustment belongs in the implied-price calculation.

## 2. Define/Discover — ELV's economics and research question

ELV earns revenue from health-insurance premiums, administration of self-funded health plans, and pharmacy and health services through Carelon. Its insured business must price coverage to cover medical claims and operating costs. Fee-based administration and Carelon provide related but different revenue streams. Commercial, Medicare and Medicaid exposure therefore matter alongside pharmacy and care-services operations when choosing peers. [ELV 2025 Form 10-K, Item 1, “Business,” overview and reportable segments](https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/elv-20251231.htm).

ELV's FY2025 reported diluted EPS is **positive at $25.21**, so the required P/E calculation is possible. This is the latest completed annual period reported by the comparison date. [ELV annual-results release, January 28, 2026, FY2025 highlights](https://www.elevancehealth.com/newsroom/elv-quarterly-earnings-q4-2025).

**Research question:** Do listed health-benefits businesses with substantial pharmacy or care-services operations provide a defensible market reference for ELV, after accounting for payer mix and unusual earnings?

The necessary research is business-segment fit, total annual GAAP diluted EPS and its publication date, same-date share prices, and material reasons reported earnings might not represent ongoing earnings power.

## 3. Represent — policy and two candidate decisions

### Initial policy carried forward from the Lab 07 ELV extension

The saved Lab 07 extension identified health-benefit exposure, payer mix, services operations, medical-cost risk and growth as the relevant criteria. The following makes those criteria operational; it is an AI-assisted elaboration, not a newly claimed before-AI student submission.

- Consider listed operating companies with material health-benefits exposure and related pharmacy or healthcare-services operations. A broad healthcare industry label alone is insufficient.
- Require USD common-share prices on September 10, 2026 and positive, total FY2025 GAAP diluted EPS published by that date. Keep adjusted earnings, quarterly results and guidance separate.
- Qualify differences in government-program exposure, services mix, geographic reach, scale, growth, leverage or unusual earnings when the core economic connection remains useful.
- Exclude a business whose economics lack a meaningful health-benefits/services connection, or whose restructuring makes the historical business a poor reference. Unverified inputs remain unresolved; nonpositive earnings cannot supply a usable P/E.
- Do not admit or remove a company because its multiple produces a preferred valuation. “QUALIFY” enters the calculation with explicit limitations; it is not a numerical discount or extra weight.

### Decisions supported by opened primary sources

| Candidate | Decision | Why it belongs; important difference | Business source and locator |
|---|---|---|---|
| UnitedHealth Group (NYSE: UNH) | **QUALIFY** | UnitedHealthcare covers employer, Medicare and Medicaid-related markets; Optum adds pharmacy and care services. This connects both sides of ELV's business. Optum also has substantial care-delivery, technology and data operations, so its business mix is not interchangeable with Carelon. Its unusual earnings charge warrants an additional qualification. | [UNH 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm), Item 1, “Our Businesses,” “Optum,” and “UnitedHealthcare”; printed pp. 1–5. Earnings issue documented below. |
| The Cigna Group (NYSE: CI) | **QUALIFY** | Cigna Healthcare combines insured and self-insured medical benefits with Evernorth's pharmacy and specialty/care services. However, Cigna sold its Medicare and related businesses to HCSC on March 19, 2025, weakening comparability with ELV's government-program exposure and changing its historical mix. | [Cigna FY2025 release](https://newsroom.thecignagroup.com/2026-02-05-The-Cigna-Group-Reports-Strong-Fourth-Quarter-and-Full-Year-2025-Results,-Establishes-2026-Outlook-and-Increases-Dividend), “Highlights of Segment Results”: “Evernorth Health Services” and “Cigna Healthcare.” |

Both candidates are retained under the policy; neither is an unqualified substitute for ELV. No investigated candidate was excluded, and no third candidate was added to influence the result. Cigna's annual-release business and EPS sections were accessible; its SEC 10-K page did not load in this research session, so the report relies on the opened company release for Cigna.

## 4. Implement — sourced company inputs

All prices are **September 10, 2026 regular-session closes**, in USD per NYSE common share. The earnings basis is **total GAAP diluted EPS for the year ended December 31, 2025**, also USD per share. All annual releases predate the valuation date. Sources below were opened on September 17, 2026; the research access date does not replace the historical valuation date.

| Company / role | Closing price | Annual reported diluted EPS | Fiscal year-end | Annual earnings publication | Price source and locator | Earnings source and locator |
|---|---:|---:|---|---|---|---|
| ELV / target | $416.54 | $25.21 | 2025-12-31 | 2026-01-28 | [ELV history](https://stockanalysis.com/stocks/elv/history/), Historical Data, **Sep 10, 2026**, **Close** column | [ELV annual release](https://www.elevancehealth.com/newsroom/elv-quarterly-earnings-q4-2025), FY2025 diluted-EPS headline; corroborated in [2025 10-K](https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/elv-20251231.htm), Consolidated Statements of Income, “Shareholders' earnings per share—Diluted,” 2025 column |
| UNH / qualified peer | $388.28 | $13.23 | 2025-12-31 | 2026-01-27 | [UNH history](https://stockanalysis.com/stocks/unh/history/), Historical Data, **Sep 10, 2026**, **Close** column | [UNH annual-results release](https://www.unitedhealthgroup.com/newsroom/2026/2026-01-27-uhg-reports-2025-results-and-issues-2026-outlook.html), full-year earnings highlights; [2025 10-K](https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm), Consolidated Statements of Operations, diluted EPS attributable to common shareholders, 2025 column |
| CI / qualified peer | $280.91 | $22.18 | 2025-12-31 | 2026-02-05 | [CI history](https://stockanalysis.com/stocks/ci/history/), Historical Data, **Sep 10, 2026**, **Close** column | [Cigna annual release](https://newsroom.thecignagroup.com/2026-02-05-The-Cigna-Group-Reports-Strong-Fourth-Quarter-and-Full-Year-2025-Results,-Establishes-2026-Outlook-and-Increases-Dividend), Exhibit 1, **Diluted Earnings Per Share / Shareholders' net income**, year ended December 31, 2025 column |

**Price convention:** Use the historical **Close**, not the dividend-adjusted close or today's quote. This matters for UNH: its September 10 Close is $388.28, while the page's adjusted close is $385.90. The three price histories are secondary market-data sources; the business and earnings evidence comes from company or SEC sources.

**Connection to the saved DCF:** Lab 06 used a September 10 after-hours ELV observation of $416.14. Lab 08 uses the same day's $416.54 regular close for all price comparisons. The $0.40 difference is disclosed, and the saved DCF—including its capital weights based on $416.14—is preserved. This is a comparison with the saved valuation, not a new DCF rerun with updated capital weights.

### Earnings quality: calculation inputs versus interpretation

- **ELV:** The 2025 effective tax rate was 15.6%, aided by a non-operating tax benefit and resolution of uncertain tax positions. Reported EPS therefore needs scrutiny as a sustainable baseline. [ELV 2025 10-K, Item 7 tax discussion and Note 8, Income Taxes](https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/elv-20251231.htm).
- **UNH:** The annual release identifies a fourth-quarter charge of $1.622 billion after tax, or $1.78 per diluted share, including cyberattack, divestiture and restructuring effects. A charge that reduces earnings increases P/E at a fixed price. [UNH FY2025 release PDF, p. 1, impact-to-earnings table](https://www.unitedhealthgroup.com/content/dam/UHG/PDF/investors/2025/unh-reports-2025-results-and-issues-2026-outlook.pdf).
- **CI:** Its reported EPS differs from adjusted operating income per share because of investment results, acquired-intangible amortization and special items. The divestiture also limits like-for-like interpretation. [Cigna annual release, Exhibit 1 reconciliation](https://newsroom.thecignagroup.com/2026-02-05-The-Cigna-Group-Reports-Strong-Fourth-Quarter-and-Full-Year-2025-Results,-Establishes-2026-Outlook-and-Increases-Dividend).

The calculation retains the required reported earnings basis throughout. Whether the three denominators represent comparable sustainable profits remains unresolved; silently replacing selected denominators with adjusted figures would not resolve it.

### Run and results

[lab08_comps.py](lab08_comps.py) is a standalone adaptation of the Lab 07 calculator with ELV, UNH and CI inputs at the top. It uses only the Python standard library and makes no network calls. The original Lab 07 files remain available.

```sh
python3 lab08_comps.py
```

| Calculation | Result |
|---|---:|
| ELV observed P/E, excluded from peer statistics | 16.522808× |
| CI P/E / minimum peer multiple | 12.665014× |
| UNH P/E / maximum peer multiple | 29.348450× |
| Median peer P/E | 21.006732× |
| ELV at minimum peer P/E | **$319.28** |
| ELV at median peer P/E | **$529.58** |
| ELV at maximum peer P/E | **$739.87** |

These are calculated values from the input table, not quoted analyst targets. With two peers, the median is the arithmetic mean of their two multiples. The low and high imply approximately **−23.35% to +77.62%** relative to ELV's $416.54 close; the median implies **+27.14%**. This spread describes two qualified market references, not a probability interval.

## 5. Validate — arithmetic and peer removal

### Independent arithmetic check

Using the sourced CI inputs:

```text
CI P/E = 280.91 / 22.18
       = 12.665013525698827... times

ELV reference = (280.91 / 22.18) × 25.21
              = 319.284990982867448... dollars
              = $319.28 displayed
```

An independent high-precision Decimal calculation agrees with the calculator's multiples, implied prices and both removal changes. Calculations use unrounded inputs and intermediate values; six-decimal multiples and cents are display formats only.

### Prediction and checked removal result

**Directional prediction:** Removing UNH, the higher-multiple peer, should lower ELV's median-implied price to CI's reference. Removing CI should raise it to UNH's reference. This follows from the formula; this AI-assisted draft does not claim a student's prediction was recorded before execution.

| Peer removed | Remaining peer | Remaining P/E | ELV reference | Change from full-peer median |
|---|---|---:|---:|---:|
| UNH | CI | 12.665014× | **$319.28** | **−$210.29** |
| CI | UNH | 29.348450× | **$739.87** | **+$210.29** |

The full-precision CI-only value is $319.284990982867… and the full-peer median estimate is $529.579713934366…. Their difference is −$210.294722951499…, displayed as **−$210.29**. Subtracting already-rounded display prices instead would give −$210.30, which is not the calculator's method.

One remaining peer gives a **reference estimate, no range**. Removing the sole peer leaves **no estimate**. Losing UNH removes evidence about a different integrated health-benefits/services business; losing CI removes the second business perspective. The $210.29 change in either direction shows substantial dependence on peer choice. Neither candidate is removed simply because of this effect.

Checks also passed for missing/nonpositive EPS, policy exclusion, duplicate tickers, target exclusion, zero/one peer behavior, and earnings publication dates preceding the valuation date. Actual command output is saved in [lab08-output.md](lab08-output.md).

## 6. Evolve — compare with DCF and judge AI criticism

| Method | ELV result and date | Main assumption or limitation |
|---|---|---|
| Week 3 DCF | **September 10, 2026:** base **$537.84/share**; saved sensitivity **$346.14–$1,036.00/share** | Starting FCFF estimate of $5,955.6 million, five forecast years ending September 10, 2027–2031, WACC 6.986920%, terminal growth 2.50%. The sensitivity changes WACC and terminal growth by ±1 percentage point; it is not a confidence interval. [Saved DCF assumptions](lab-06-elv.md) and [calculator](dcf.py). |
| Peer P/E | **September 10, 2026 closes:** **$319.28–$739.87/share**, median **$529.58/share** | Two qualified peers and FY2025 total GAAP diluted EPS. Business mix and earnings quality differ; one peer removal eliminates the range. Sources and calculations appear above. |

Both final outputs value **ELV common equity per share**. The DCF first values enterprise cash flow and then makes its existing equity bridge; the P/E calculation directly values equity. Their forecast bases differ: forward estimated cash flow versus historical reported annual earnings. Each denominator follows its own method; no new adjustment is made for the DCF's quarterly diluted-share count versus the annual EPS share counts.

The DCF base exceeds the peer median by only **$8.26/share**, but closeness does not validate the forecasts or peer selection. A broad peer spread can contain the DCF base without strong agreement. The comparison adds a market-based challenge to the cash-flow model: CI's reference is below the observed price while UNH's is well above it. I do not mechanically average the two valuation methods.

**Provisional call and evidence that could change it:** Watch-defer. Evidence of sustained cash-flow conversion and a defensible reconciliation of unusual earnings would matter more than the small gap between the median and DCF.

### AI skeptical review and source-checked response

The following is the skeptical review performed for this draft, followed by proposed judgments of the criticism. It is not a fabricated transcript from a human partner or a second independent AI session.

**Review:** The weakest supported assumption is that the median of these two reported P/Es represents sustainable ELV earnings power. There is also a major forecast dependence in the DCF: the starting FCFF estimate is 36.47% above the historical FY2025 FCFF of $4,364.04 million. Matching dollars per share and calendar dates does not make historical GAAP earnings economically identical to forward normalized cash flow.

| Criticism | Judgment | Evidence and consequence |
|---|---|---|
| The apparent DCF/median agreement is weak because the peer set is small and earnings quality differs. | **ACCEPT** | Removing either peer moves the estimate $210.29. The tax and charge evidence in Section 4 shows why equal accounting labels do not guarantee equal sustainability. Keep both qualifications and withhold a narrow fair-value claim. |
| The DCF's recovery assumption needs operating evidence. | **ACCEPT** | [dcf.py](dcf.py) contains the $5,955.6 million starting estimate. ELV's [July 15, 2026 release](https://www.sec.gov/Archives/edgar/data/1156039/000115603926000058/a2q2026elvearningsrelease.htm), p. 1, supports the $6.0 billion operating-cash-flow guidance floor used in it, but guidance is not realized cash flow; subsequent forecasts remain analyst estimates. |
| The price observations are not identical to the saved DCF quote. | **ACCEPT; DISCLOSED** | The saved model uses $416.14 after hours; the source table uses $416.54 regular close. Same-date regular closes are used consistently for the peer comparison, and the DCF is explicitly labeled as saved. |
| These outputs must be compared as enterprise values or P/E must be adjusted for debt. | **REJECT** | The DCF output already includes its equity bridge and share division; peer P/E already gives common-equity value per share. Adding another debt adjustment would mix valuation objects. |
| The peer earnings can be treated as fully normalized because all are reported GAAP. | **REJECT** | Section 4 documents specific unusual items. The correct sustainable earnings levels and their effect on relative valuation remain **UNRESOLVED** pending a consistent reconciliation. |

**AI question that could change the decision:** If ELV's expected cash-flow recovery is not realized, would you still initiate because its price is below the peer median?

**Proposed answer:** No. The median is highly sensitive to two different peer businesses, and the DCF depends on recovery. I would require stronger operating evidence before treating either central estimate as a sufficient margin of safety. The next reports should be checked against the July cash-flow outlook, the cash-flow forecasts in the saved model, and the medical-cost and membership concerns carried forward from Lab 06.

## 7. Reflect — conclusion to defend

**Decision: watch-defer.** I can defend **$319.28–$739.87** as the conditional range generated by the two qualified peers and sourced annual EPS. I cannot defend it as a narrow intrinsic-value interval or claim that its upper end is a likely outcome. The saved DCF remains **$537.84**, with its separately identified **$346.14–$1,036.00** sensitivity range.

The peers belong because each combines health benefits with related services; the qualifications in Section 3 explain why their multiples cannot be transferred without judgment. P/E adds an observed market comparison to the DCF, and the removal exercise exposes how much the central result depends on the two selected businesses.

**What would change my call:** I would consider initiate if subsequent reporting supports sustained medical-cost improvement and membership stabilization, cash generation supports the saved forecast, and a consistent review of earnings quality leaves a persuasive valuation case at the then-current price. I would move toward do not initiate if recovery assumptions fail and the investment case remains dependent on the highest peer multiple. These are proposed decision criteria, not company guidance or completed future observations.

**Practice partner question:** “If the DCF and peer median both suggest upside, why wait?”  
**Answer:** Their agreement is not independent proof. The DCF is heavily dependent on terminal assumptions, while each peer removal changes the P/E estimate by roughly $210 per share. I need operating evidence that supports the earnings and cash flows being valued.

## 8. Checkout

Files prepared:

- [lab-08-elv.md](lab-08-elv.md): company analysis, policy, sources, validation, comparison and proposed judgment.
- [lab08_comps.py](lab08_comps.py): standalone ELV calculator with editable inputs.
- [lab08-output.md](lab08-output.md): captured calculator and saved DCF output.

Run the new calculation from the project folder with `python3 lab08_comps.py`.

**Student checkout remains:** Review and own the policy and judgments, complete the actual class discussion and any instructor-required independent AI comparison, and submit the files' GitHub links through the Lab 08 checkout when instructed. The local files are prepared; no GitHub upload or Brightspace submission has been performed.
