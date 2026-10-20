# Submission checklist — ELV package

The local technical package is built for **Elevance Health (ELV)**. Full course submission remains incomplete because required human evidence and instructor disposition are not supplied. Nothing has been uploaded, recorded or submitted by this rebuild.

## Architecture status — visible, not silently marked complete

The preserved research/ASSIGNMENT.md excludes insurers and requires FCFF/WACC, an enterprise-to-equity bridge and an enterprise multiple. This requested ELV build uses FCFE/cost of equity and P/E, consistent with the earlier ELV labs. It does not claim those different requirements are satisfied. Record the instructor’s acceptance of an insurer architecture or the permitted remedy. No exception is assumed, and ELV has not been switched to another company.

## Seven-part bundle (provisional filenames)

| Component | ELV files prepared | Remaining work |
|---|---|---|
| Original Edition A plus Edition B | EDITION_B.md, RESEARCH_EVOLUTION.md, COMMITTEE_MEMO.md; labeled retrospective reflection in research/ | Review the new AI-assisted Edition B and match its format to the official checklist. Attach the actual unchanged original checkpoint and receipt. The retrospective reflection is not that checkpoint. |
| Runnable repository / visible output | START_HERE.md, model.py, elv_forecast.py, app.py, index.html, outputs/BASE_REPORT.html, BASE_REPORT.md, BASE_RUN.json | Publish/share only as the course requires, verify grader access and exact official filenames |
| Research-evolution Video 1 | VIDEO_1_SCRIPT.md and RESEARCH_EVOLUTION.md | Review, record and correct the actual transcript; show genuine history |
| Code/validation Video 2 | VIDEO_2_SCRIPT.md, test_model.py, cold_run.py, submission_checks.py | Record execution and explanation; attach actual locked human prediction |
| Memo/deck | COMMITTEE_MEMO.md | Review and own the judgment; confirm whether memo alone meets official format |
| Committee Video 3 | VIDEO_PLAYBOOK.md and working ELV demo | Open with live margin change → result → reset → failure → recovery, then defend the range; correct transcript |
| Frozen validation / AI-use record | records/AI_USE_AND_VALIDATION.md, ASSUMPTION_CHALLENGE.md, AI_DIRECTIONAL_PRECOMMIT.md, COLD_RUN.log, SUBMISSION_CHECKS.log, MANIFEST.json | Add genuine human records, resolve course departures, check access, regenerate manifest after final edits, submit and retain receipt |

## Requirement mapping

| Brief requirement | ELV implementation | Status |
|---|---|---|
| 1 User, security, dates, units, shares | MODEL_GUIDE.md, metadata, app, memo | Implemented; dates clearly separated |
| 2 Provenance and normalization | HISTORICAL_INPUTS.json, SOURCES.json, filing checks, normalization catalog | Implemented with D&A scope and insurer-capital limitations disclosed |
| 3 Company-specific five-year linked statements | Revenue, benefits, product costs, claims, investments, equity, cash; fail-loud checks | Implemented as simplified consolidated ELV forecast |
| 4 Pro-forma FCFF/WACC/enterprise bridge | Direct FCFE/cost-of-equity valuation | **Departure: instructor acceptance unresolved** |
| 5 Cases, discount/growth grid, terminal share, reverse DCF | ELV cases; cost-of-equity/g grid; retrospective origin-date reverse solver | Implemented with cost of equity replacing WACC; acceptance unresolved |
| 6 Consistent EV and equity multiples | Qualified UNH/CI P/E, leave-one-out analysis | **P/E implemented; EV multiple omitted under insurer architecture** |
| 7 Method disagreement | MODEL_GUIDE.md, memo, peer policy | Implemented; dates, earnings and methods not mechanically averaged |
| 8 Own-model OAT, ranges and challenge record | Two ranges; operating-profit, FCFE and value rankings | Implemented; genuine partner evidence pending |
| 9 Conditional range and action | Memo and live overview | Draft judgment requires student review |
| 10 Usable bounded product | Driver panel, reset, outputs, visible checks, failure diagnostics, export | Implemented |

## Validation mapping

| Required validation | Evidence / limitation |
|---|---|
| Synthetic/known answer | New $1000 equity perpetuity reconciliation and regression to existing ELV Lab 10. Not claimed as the official course training-case answer; confirm accepted proof |
| Independent source/definition check | Filing rows and close-versus-adjusted-close checks documented in AI_USE_AND_VALIDATION.md; not an independent human review |
| Directional test before execution | AI_DIRECTIONAL_PRECOMMIT.md plus executable tests; explicitly AI-authored |
| Locked human AI-off record | **Pending authentic original evidence** in HUMAN_RECORDS.md |
| Articulation, boundaries and valuation reconciliation | test_model.py; Checks tab; saved report |
| Peer definitions | ELV/UNH/CI GAAP EPS and same-date close; PEER_POLICY.md |
| High-risk failure and cold run | Insufficient liquidity, broken cash, terminal rejection; actual COLD_RUN.log |
| Corrected/qualified AI output | Wrong-company build corrected; insurer capital and negative-flow conventions qualified in AI-use record |

## Before final submission

- [ ] Obtain and record instructor disposition of ELV eligibility, FCFE architecture, missing EV multiple and permitted synthetic proof.
- [ ] Attach the original unchanged Edition A and first successful checkpoint receipt.
- [ ] Attach genuine human-authored AI-off prediction/precommit, actual comparison and decision effect. Do not backdate or use AI’s demonstrated prediction as your own.
- [ ] Add credited real partner challenges and your response.
- [ ] Review statutory capital, parent dividend capacity, refinancing, margin recovery, D&A scope and terminal reinvestment assumptions.
- [ ] Match all filenames, duration limits, Edition B format and submission destinations to the official shared checklist, which was not supplied here.
- [ ] Record three distinct ELV videos; correct transcripts against the actual audio.
- [ ] Check repository, source and video access from the grader’s perspective.
- [ ] Run the verification commands below; review every warning and open item.
- [ ] Regenerate the manifest after final edits, submit to the correct assignment and save the receipt.

```sh
python3 -m unittest -v
python3 build_report.py
python3 submission_checks.py
python3 cold_run.py
python3 freeze_manifest.py
```

`submission_checks.py` returns a technical pass/fail for the ELV files and saved values. It separately reports **COURSE SUBMISSION INCOMPLETE** while required human/course evidence is pending. It never treats a green model as a submission receipt.
