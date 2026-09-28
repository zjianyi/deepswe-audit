# State

- Frozen corpus: 113 tasks and the original ten-task pilot. Upstream and Pier pins unchanged; no upstream repairs or model-solving trials.
- Phase 1: 97 PASS, 16 FAIL; 113 reproducibility warnings. Prior checks: 112 BTQC tests, 17 audit tests, actionlint.
- Smoke 36353718484 and all nine jobs in 36356902711 completed. All ten native bundles downloaded, hash-verified and imported.
- All nine executable oracle/no-op pairs passed (1/0), retaining native nonzero no-op partial credit. KaTeX blocked before execution by registry rate limiting.
- Raw imported execution statuses: two FAIL (GoReleaser, Helm protected writes), three INFRASTRUCTURE_FAILURE (KaTeX, Dateutil, fd), five DEFERRED_EVIDENCE_REQUIRED (unobserved probe reach).
- Independent raw-evidence inspection found Dateutil and fd protected-path probes accepted by Pier with reward 1 and no exception despite absent CTRF. Separate hash-bound audit annotations record these demonstrated reward bypasses; original importer classifications remain preserved. Four tasks therefore have concrete integrity findings, independent of raw aggregate labels.
- GoReleaser and Helm also exhibit inflated report-forgery partial credit with binary reward 0.
- Nine S0 reviews completed as of 2026-09-28 00:14 UTC: GoReleaser deferred, Helm FAIL, Testem deferred, KaTeX deferred, Bandit FAIL, Dateutil deferred, fd FAIL (reviewer flags random-sort and timestamp coverage gaps), wasmi deferred, awilix deferred. Raw reviews preserved; annotations distinguish reviewer errors and interpretive findings from demonstrated exploits.
- Sequential review queue active: exec session 25269, shell PID 92260. happy-dom currently running as the final review. Do not launch duplicate reviews while this queue is active.
- Zero clean three-phase results. Detailed local evidence retained. One-minute monitor active.
- No native retries used. No documented registry correction yet; KaTeX remains explicitly blocked. Banana Bench unchanged.
