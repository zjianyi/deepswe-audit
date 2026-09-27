# Decisions

- Audit upstream commit 0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea with Pier 0.3.1.
- Preserve all upstream task bytes; diagnostic attacks are separately hashed overlays.
- Public runner code has no dependency on private BTQC; normalize evidence locally.
- No upstream repair, paid model trial, or cohort replacement.
- Initial adapter testing required 40-character base commit strings. Inspection found three matching abbreviated Git SHAs, so the adapter accepts 7–40 hexadecimal characters and reports unresolved canonical identity as a reproducibility warning. This corrects an adapter assumption; no upstream file or existing BTQC policy was changed.
- Pier 0.3.1 stops the agent before separate verifier startup. Memory preflight therefore requires one 8-GiB allocation plus host headroom, not two simultaneous allocations. Disk preflight requires 25 GiB free both before and after the image pull.
- DeepSWE test assertions and oracle implementations live in patch files. The semantic bundle now includes `.patch` and `.diff` as inert text, with regression coverage.
