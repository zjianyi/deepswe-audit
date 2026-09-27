# State

- Frozen corpus: 113 tasks; deterministic ten-task pilot. Upstream and Pier pins unchanged.
- Phase 1: 97 PASS, 16 FAIL; 113 reproducibility warnings.
- Integration checks previously passed: 112 BTQC tests, 17 audit tests, actionlint.
- Smoke run 36353718484 completed and imported: oracle reward 1, no-op reward 0 with valid partial credit 0.5. Execution FAIL: candidate code modified protected verifier surfaces. Report forgery produced partial credit 0.9827586206896551 but binary reward 0.
- GoReleaser S0 semantic review completed: DEFERRED_EVIDENCE_REQUIRED. Original output preserved. Separate audit annotation records its incorrect interpretation of protected writes and scope mismatch concerning a mutant campaign.
- Remaining run 36356902711: Helm, Testem, and KaTeX completed and imported; Bandit running, five queued as of 2026-09-27 23:16 UTC. Helm execution FAIL: oracle 1/no-op 0, protected verifier write observed; forged reports raised partial credit from 0.2033898305084746 to 0.8135593220338984 with binary reward 0.
- Helm S0 completed: FAIL (mixed-array ordering finding); separate annotation flags its false missing-execution claims and unresolved contract interpretation. Testem S0 is active (exec session 9299). KaTeX S0 is next and must include its blocker; six further reviews await execution evidence.
- One-minute heartbeat deepswe-audit-progress is active; notify only meaningful changes.
- Report and evidence summary updated: 4/10 execution outcomes, 2/10 semantic outcomes, zero clean three-phase results.
- No upstream task modified, valid failure retried, or model-solving trial run. Banana Bench unchanged.

- Testem endpoints pass (oracle 1/no-op 0); all three probes lacked reach markers, so execution remains DEFERRED_EVIDENCE_REQUIRED.
- KaTeX execution is INFRASTRUCTURE_FAILURE: image pull was registry rate-limited (not evidence of a missing image). No cases ran; no retry yet, pending documented cause correction and serial-run completion.
