# State

- Frozen corpus: 113 tasks and the original ten-task pilot. Upstream and Pier pins unchanged; no upstream repairs or model-solving trials.
- Phase 1: 97 PASS, 16 FAIL; 113 reproducibility warnings. Prior checks: 112 BTQC tests, 17 audit tests, actionlint.
- Smoke 36353718484 and all nine jobs in 36356902711 completed. All ten native bundles downloaded, hash-verified and imported.
- All nine executable oracle/no-op pairs passed (1/0), retaining native nonzero no-op partial credit. KaTeX blocked before execution by registry rate limiting.
- Raw imported execution statuses: two FAIL (GoReleaser, Helm protected writes), three INFRASTRUCTURE_FAILURE (KaTeX, Dateutil, fd), five DEFERRED_EVIDENCE_REQUIRED (unobserved probe reach).
- Independent raw-evidence inspection found Dateutil and fd protected-path probes accepted by Pier with reward 1 and no exception despite absent CTRF. Separate hash-bound audit annotations record these demonstrated reward bypasses; original importer classifications remain preserved. Four tasks therefore have concrete integrity findings, independent of raw aggregate labels.
- GoReleaser and Helm also exhibit inflated report-forgery partial credit with binary reward 0.
- Ten S0 attempts recorded: nine validated reviews (three FAIL, six DEFERRED_EVIDENCE_REQUIRED), one INFRASTRUCTURE_FAILURE. Happy DOM output failed strict SEM-020 validation; no rerun. No semantic processes remain.
- All scheduled items accounted for. Zero clean three-phase results. Final REPORT.md, ten per-task evidence folders, 113-task inventory, static findings and reproducible manifests/run.json published; detailed source/native/input bundles retained locally.
- Final validation: 19 public tests, actionlint and git diff checks pass; all 113 source, framework/context and ten artifact bindings verified. Earlier private BTQC regression suite: 112 passed. No shared policy or frozen runtime altered during final reporting.
- Pilot monitoring was paused after final publication; subsequently resumed for the separately authorized expansion below.
- No native retries used. No documented registry correction yet; KaTeX remains explicitly blocked. Banana Bench unchanged.

## Authorized expansion

- User authorized all remaining 103 tasks. Frozen complement: manifests/expansion.json, hash 2549850b9966d0e4322e575c937486292512dfd976b102991fe110f68d59031c. Existing corpus and pilot manifests unchanged.
- Expansion workflow and sequential local worker implemented. Phase 1 already covers all 103; local static envelopes gain frozen codebase context before evidence import, with original envelopes retained locally.
- Expansion-only driver captures native reward/Pier acceptance even without final CTRF; accepted candidate attack reward is a failure. S0 wrapper archives raw output and uses an attempt marker to prevent repeats. Frozen BTQC source, rubric and validation unchanged.
- Validation: 23 public fixtures and actionlint pass; first expansion task context/static prepared; original pilot evidence hashes verified unchanged.
- Expansion run 36363797336 dispatched at e0f63ae14f4fbd4ad74d615372ec720f3609b33c: abs-module-cache-flags running, 102 queued at launch. URL: https://github.com/zjianyi/deepswe-audit/actions/runs/36363797336
- Sequential local worker active: PID 99581, exec session 18701, scripts/expansion.py work --run 36363797336. It downloads/imports completed jobs, prepares immutable context/static evidence and executes one S0 per task. Inspect lock/process and durable attempt markers before any restart.
- One-minute automation deepswe-audit-progress updated and ACTIVE for this expansion, with meaningful-change notifications only.

- Expansion checkpoint 2026-09-28 08:05 UTC: seventy-two native task jobs completed on GitHub; psd-tools-blend-range-api running and 30 queued (setup excluded). Recorded local outcomes: {'execution': 72, 'semantic': 72, 'static': 103}; zero clean results. Phase status counts: {"execution": {"DEFERRED_EVIDENCE_REQUIRED": 18, "FAIL": 40, "INFRASTRUCTURE_FAILURE": 14, "NOT_RUN": 31}, "semantic": {"DEFERRED_EVIDENCE_REQUIRED": 21, "FAIL": 34, "INFRASTRUCTURE_FAILURE": 17, "NOT_RUN": 31}, "static": {"FAIL": 16, "PASS": 87}}. Prometheus typed-label sorting S0 failed strict SEM-020 validation because its actionable verdict lacked a finding; raw review archived and first outcome preserved. Native protected-path reward bypass remains independently supported. Original worker PID 99581 waiting normally with no active S0 or worker/poll errors. No retries; pilot unchanged.

- Authorized subagents completed read-only reconciliation: 532 native artifact hashes match across the first six tasks; cohort, summary and six archived S0 bindings validated. Supporting raw-file hashes published in evidence/expansion-reconciliation-first-six.json. Two crash-recovery guards implemented: refuse started S0 before rewriting input, and restore a missing public result from the preserved local outcome without rereview. All 27 public tests pass. Active worker left uninterrupted; changes apply on subsequent process loads.

- Second independent reconciliation batch verified 284/284 artifact hashes for tasks 7–9; no discrepancies. Total independently reconciled artifacts: 816 across nine tasks.

- Third independent reconciliation batch verified 171/171 artifacts for tasks 10–14; public/raw bindings and case fields match. Total 987 artifacts across fourteen tasks, no discrepancies.

- Fourth independent reconciliation batch verified 403/403 artifacts for tasks 15–19; total 1,390 artifacts across nineteen tasks, no discrepancies.

- Fifth independent reconciliation batch verified 200/200 artifacts for tasks 20–24; total 1,590 across twenty-four tasks, no discrepancies.

- Sixth independent reconciliation batch verified 268/268 artifacts for tasks 25–29; total 1,858 across twenty-nine tasks. Raw report-forgery false positives confirmed for Geo and Go-critic, no discrepancies.

- Seventh independent reconciliation verified 454/454 artifacts for tasks 30–34; total 2,312 across thirty-four tasks, no discrepancies. GQL raw failing-test log corroborates reward bypass despite missing attribution markers.

- Eighth independent reconciliation verified 439/439 artifacts for tasks 35–39; cumulative 2,751 across thirty-nine tasks, no discrepancies.

- Ninth independent reconciliation verified 427/427 artifacts for tasks 40–44; cumulative 3,178 across forty-four tasks, no discrepancies.

- Tenth independent reconciliation verified 386/386 artifacts for tasks 45–49; cumulative 3,564 across forty-nine tasks, no discrepancies.

- Eleventh independent reconciliation verified 503/503 artifacts for tasks 50–54; cumulative 4,067 across fifty-four tasks, no discrepancies.

- Twelfth independent reconciliation verified 340/340 artifacts for tasks 55–59; cumulative 4,407 across fifty-nine tasks, no discrepancies.

- Thirteenth independent reconciliation verified 376/376 artifacts for tasks 60–64; cumulative 4,783 across sixty-four tasks, no discrepancies.

- Fourteenth independent reconciliation verified 289/289 artifacts for tasks 65–69; cumulative 5,072 across sixty-nine tasks, no discrepancies.
