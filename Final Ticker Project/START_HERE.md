# Start here — Elevance Health (ELV)

This is your **ELV** final project: a local workbench, saved outputs, committee memo, research-evolution narrative, video scripts, validation records and submission checks. It extends the ELV model from Labs 10–11.

## 1. Open the ELV model

Double-click **Launch Workbench.command** in this folder. Keep Terminal open. The browser opens at **http://127.0.0.1:8765**.

If needed, paste this in Terminal:

```sh
cd '/Users/davidzarate/Downloads/AI in finance/Final Ticker Project'
python3 app.py
```

Use Python 3.9 or newer. No package installation, account or internet is required for model calculations. If an older workbench is still running, stop its Terminal with Control+C before launching this version. Confirm the page title says **ELV · Equity Pro-Forma Workbench**. If the port is occupied, use `python3 app.py --port 8766`. Refresh the browser after restarting.

Do not double-click index.html: it needs the Python server. To read results without running Python, open **outputs/BASE_REPORT.html**. Browser changes are temporary; **Export this run** downloads an ELV JSON snapshot.

## 2. Practice the five-minute demonstration

1. Click **Reset to base**. Confirm value **$365.24**, FY2030 operating profit **8,479.6**, FCFE **6,116.8** and terminal share **74.9%**.
2. Set **Blended gross margin shift** to **0.50**, then press Tab, or click **1 · Margin shift → +0.50 pp**. Every annual margin rises 0.50 percentage points; the shortcut starts from base. Value becomes **$378.82**, profit **8,823.1**, FCFE **6,374.5**.
3. Open **Three statements**. Trace operating revenue → benefits/product costs → blended gross profit → operating income → net income → receivables/claims changes → CFO → FCFE. This margin is not medical benefit ratio.
4. Click **2 · Restore base** and confirm **$365.24**.
5. Click **3 · Inject cash error**. Value reads **WITHHELD**. In **Checks**, FY2026 balance-sheet and cash-flow gaps are both **−100.000000**. This deliberately removes $100m of cash without a cash-flow transaction. Click Reset to recover.
6. Open **Sensitivity**. Compare **Full control range** with **Alternative local range**; switch between operating profit, FCFE and value. A driver’s rank depends on the range. Invalid endpoints are excluded.
7. Open **Assumptions & evidence**. Read a control’s value, basis, challenge and revision evidence. Sources link to ELV, UNH and Cigna evidence.
8. Return to **Decision & valuation**. Explain the conditional range and the separate dates of the equity DCF and peer reference.

Use a wide browser window for recording so the driver and output remain visible. Practice once before recording. Do not edit Python during the live product demo.

## 3. Read these next

| File | Purpose |
|---|---|
| MODEL_GUIDE.md | ELV accounting, FCFE valuation, dates, share basis and limitations |
| outputs/BASE_REPORT.html | Complete numerical output without code execution |
| COMMITTEE_MEMO.md | ELV recommendation draft to review and own |
| RESEARCH_EVOLUTION.md | How the saved ELV research led to this model |
| VIDEO_1_SCRIPT.md | Research-evolution recording script |
| VIDEO_2_SCRIPT.md | Code and validation recording script |
| VIDEO_3_SCRIPT.md | Read-aloud live demonstration and committee defense script |
| VIDEO_PLAYBOOK.md | Preparation and Video 3 live committee script |
| SUBMISSION_CHECKLIST.md | ELV deliverables, course departures and remaining human evidence |
| records/AI_USE_AND_VALIDATION.md | Corrections and actual validation scope |
| records/HUMAN_RECORDS.md | Authentic checkpoint, prediction, partner and recording evidence |

## 4. Understand the dates and submission boundary

The DCF is a retrospective **December 31, 2025** exercise using the FY2025 filing published **February 6, 2026**. Its reverse DCF uses the **$350.55 December 31 close**. Peer P/E uses separately labeled **September 10, 2026** prices. This is not a current October 2026 price target.

The supplied brief expressly excludes insurers and requires FCFF/WACC and enterprise multiples. ELV is retained as you requested. The checklist marks these requirements as an unresolved architecture departure; no instructor exception is assumed. This does not stop you from operating or reviewing the ELV package.

Your existing `edition A.md` is an AI-assisted retrospective reflection and says it is not the original checkpoint. A labeled copy is in research/. It cannot replace the unchanged AI-off checkpoint or its receipt.

## 5. Reproduce and freeze

```sh
python3 -m unittest -v
python3 build_report.py
python3 submission_checks.py
python3 cold_run.py
python3 freeze_manifest.py
```

The cold run copies the project into a fresh standard-library-only environment, tests the ELV engine and HTTP endpoints, and writes records/COLD_RUN.log. Submission checks verify the local ELV package; a technical PASS does not complete the course submission. Record videos, correct actual transcripts, attach genuine human records and follow the official filename checklist before final freezing and submission.
