# ELV — AI use and validation record

Rebuild date: October 19, 2026. AI-assisted technical work and proposed finance judgments; not independent student work or a human AI-off checkpoint.

## Corrected AI output

The previous final package used a different company, even though the user’s research target was ELV. The user identified the mismatch and explicitly requested all materials be based on ELV. The correction replaced the active accounting/valuation model, drivers, peers, UI, saved reports, guides, memo, video scripts and submission checks. The old package is archived outside the active project. The assignment text is preserved because its insurer exclusion is a real unresolved conflict.

## Evidence and definition checks actually performed

- Opened ELV FY2025 SEC 10-K; checked consolidated operating revenue, benefit/product expenses, reported pretax/tax/common income, balance-sheet rows and 220,723,898 year-end common shares.
- Reconciled assets 121494, liabilities 77468, common equity 43882 and NCI 144. Opening aggregated model rows are checked against individually transcribed filing rows.
- Checked cash roll-forward: opening 8288 + CFO 4290 − investing use 1344 − financing use 1738 − FX 5 =9491.
- Verified ELV’s origin-date unadjusted close 350.55 from ChartExchange, with Yahoo search-result history as a cross-check. Adjusted-price results were not substituted.
- Reopened September 10, 2026 close rows for ELV 416.54, UNH 388.28 and CI 280.91. UNH adjusted close 385.90 is not the chosen input.
- Reopened UNH/Cigna annual releases for FY2025 reported EPS 13.23 /22.18; ELV EPS 25.21 is in the filing. No adjusted EPS substitutes.
- PP&E D&A selection and 2023–2024 history are carried from the saved Lab 10. The 979+628 versus reported CFO D&A 1546 scope difference remains unresolved and is displayed in the normalization catalog.

Source links, dates and locators: research/SOURCES.json. These are AI-assisted document/arithmetic checks, not a claim that a second human independently checked the model.

## Model corrections and qualifications

The model uses ELV’s medical claims, investment income and equity funding mechanics. FCFE is discounted at cost of equity, with no second debt subtraction or unproven addition of consolidated investment assets. Blended margin is not medical benefit ratio.

Signed negative interim FCFE is retained, correcting the older lab positive-only convention. The base remains **$365.24** because its cash flows are positive. A terminal debt-paydown addback and the missing statutory-capital reinvestment schedule remain disclosed limitations. Liquidity-only revolver proceeds are excluded from valued FCFE and draw scenarios are flagged.

## Executed checks and reproduction

`python3 -m unittest -v` passes the ELV suite covering synthetic valuation, original Lab 10 regression, filing mappings, all three scenarios, directionality, claims timing, interest sensitivity, boundaries, signed negative cash flows, broken cash, funding shortfall, reset, peers, reverse solving and JSON/UI target identity. `records/COLD_RUN.log` records the actual final fresh-environment run; `records/SUBMISSION_CHECKS.log` records the local package checks. Neither is a student precommit.

Base value **$365.238954**. Margin shift +0.50 pp gives **$378.818003**; FY2030 profit changes by **343.581013 million** and FCFE by **257.757496 million**. Cash corruption produces both FY2026 gaps of −100 and withheld value. The AI-authored directional specification was saved before the new tests were executed.

The $1000 synthetic known answer is an algebraic test, not the official course starter answer. The independent-source check is independent of the calculator, not independent of AI authorship. Course acceptance of the adapted validation evidence remains on the checklist.

## Human and course boundaries

The current `edition A.md` is an explicitly AI-assisted retrospective reflection, not the original checkpoint. No original human prediction, timestamp/commit, partner exchange, recording, corrected transcript, external access result, instructor exception or submission receipt has been invented. See HUMAN_RECORDS.md.

The brief excludes insurers and requires an enterprise architecture. User authorization establishes ELV as the build target, but does not establish instructor approval. SUBMISSION_CHECKLIST.md preserves that distinction. MANIFEST.json records the current build’s checksums only.
