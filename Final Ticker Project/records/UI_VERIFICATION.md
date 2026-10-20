# ELV browser verification — October 19, 2026

Checked the rebuilt local workbench in native Google Chrome at http://127.0.0.1:8766 using actual UI controls. This is an AI-operated check, not a student recording.

- Page title and header identify ELV / Elevance Health.
- Base metrics displayed $365.24, FY2030 operating profit 8,479.6 million, FCFE 6,116.8 million and terminal share 74.9%.
- Clicking Margin shift → +0.50 pp displayed $378.82, profit 8,823.1 million, FCFE 6,374.5 million and value change $13.58.
- Screenshot inspection showed readable metric cards, demonstration controls and navigation in the responsive layout.
- Corrected slider rounding discovered during inspection: sliders now preserve exact base inputs (including capex 1,116 and claims timing 42.06945), matching the numeric fields instead of rounding to an increment before interaction. Backend bounds remain enforced.
- After reload, the base values and exact slider inputs were confirmed again.
- Clicking Inject cash error and Checks visibly displayed WITHHELD, a FY2026 balance-sheet FAIL of −100.000000 and cash-flow FAIL of −100.000000.
- Restore base returned $365.24. The Sensitivity panel displayed the output ranking and excluded the invalid endpoint. The range menu successfully changed to Alternative local range.

HTTP validation, all financial tests, report generation and reset/bad-input handling are separately recorded in COLD_RUN.log. No full graphical audit of every possible driver combination or browser is claimed. No export download, external submission or student video was created during this check.
