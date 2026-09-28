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
- One-minute monitoring is ready to pause after final publication; no unfinished execution or review jobs.
- No native retries used. No documented registry correction yet; KaTeX remains explicitly blocked. Banana Bench unchanged.
