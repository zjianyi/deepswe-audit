# Decisions

- Audit upstream commit 0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea with Pier 0.3.1.
- Preserve all upstream task bytes; diagnostic attacks are separately hashed overlays.
- Public runner code has no dependency on private BTQC; normalize evidence locally.
- No upstream repair, paid model trial, or cohort replacement.
- Initial adapter testing required 40-character base commit strings. Inspection found three matching abbreviated Git SHAs, so the adapter accepts 7–40 hexadecimal characters and reports unresolved canonical identity as a reproducibility warning. This corrects an adapter assumption; no upstream file or existing BTQC policy was changed.
- Pier 0.3.1 stops the agent before separate verifier startup. Memory preflight therefore requires one 8-GiB allocation plus host headroom, not two simultaneous allocations. Disk preflight requires 25 GiB free both before and after the image pull.
- DeepSWE test assertions and oracle implementations live in patch files. The semantic bundle now includes `.patch` and `.diff` as inert text, with regression coverage.
- Native evidence is imported only after artifact hashes, case-manifest equality, image identity and exact permitted derivative-task bytes validate. The effective derivative changes only image resolution for endpoints; probes additionally replace the solver script with a separately hashed candidate-only hook.
- Static scoring validation is AST-only. All 113 released grader files share SHA-256 47cc9eaadf21e636323c360ec4fa786f0733ec9fd1d21ea5a5717ff9f8c4077c. No native task passability or resistance claim follows from this common source identity.

- Preserve the first S0 exactly even when its interpretation conflicts with raw execution evidence. Record discrepancies in a separate audit annotation; do not rerun S0 or expand into its requested 8–12-mutant campaign. Protected writes remain a concrete execution failure.
- KaTeX IMAGE_UNAVAILABLE is caused by registry rate limiting in image-pull.log, not a confirmed absent image. Retain the attempt; any single infrastructure retry requires a documented correction and must preserve one native task at a time.
- A missing CTRF invalidates evaluation credit but does not erase a native reward-bypass finding: Dateutil and fd protected-paths trials contain reward 1 accepted by Pier without exceptions. Preserve frozen importer and S0 outputs; publish separate hash-bound annotations and disclose the importer limitation.
