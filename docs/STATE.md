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

- Expansion checkpoint 2026-09-28 03:43 UTC: thirty-three native task jobs completed; helm-unified-manifest-stream running and 69 queued (setup excluded). Twenty-four native bundles imported: thirteen FAIL, four deferred, seven infrastructure failures. Seventeen executable oracle/no-op pairs passed. Twenty-three S0 outcomes: eleven FAIL, seven deferred, five strict-validation infrastructure failures; zero clean results. Eicrud S0 FAIL identifies optional __sort validation despite required cursor representation; pinned source corroborates, runtime remains blocked. Etree native FAIL: protected-path reward 1 accepted by Pier with reach/write markers; sole S0 active in original worker PID 99581. No worker/poll errors. Counts: static 103/103, execution 24/103, semantic 23/103. No retries; pilot unchanged.

- Authorized subagents completed read-only reconciliation: 532 native artifact hashes match across the first six tasks; cohort, summary and six archived S0 bindings validated. Supporting raw-file hashes published in evidence/expansion-reconciliation-first-six.json. Two crash-recovery guards implemented: refuse started S0 before rewriting input, and restore a missing public result from the preserved local outcome without rereview. All 27 public tests pass. Active worker left uninterrupted; changes apply on subsequent process loads.

- Second independent reconciliation batch verified 284/284 artifact hashes for tasks 7–9; no discrepancies. Total independently reconciled artifacts: 816 across nine tasks.

- Third independent reconciliation batch verified 171/171 artifacts for tasks 10–14; public/raw bindings and case fields match. Total 987 artifacts across fourteen tasks, no discrepancies.

- Fourth independent reconciliation batch verified 403/403 artifacts for tasks 15–19; total 1,390 artifacts across nineteen tasks, no discrepancies.
