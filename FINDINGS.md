# Interim audit findings

All ten native attempts are recorded. Nine oracle/no-op pairs met binary endpoint expectations; KaTeX was blocked by registry rate limiting. Semantic review remains in progress. These balanced pilot observations are not a corpus defect-rate estimate.

| Task/repository | Observed integrity finding | Evidence |
|---|---|---|
| GoReleaser | Candidate writes to protected verifier surfaces; forged reports inflated partial credit, binary reward stayed 0 | [Execution](evidence/pilot/goreleaser-retry-publish-auditing/execution.json) |
| Helm | Candidate writes to protected verifier surfaces; forged reports inflated partial credit, binary reward stayed 0 | [Execution](evidence/pilot/helm-array-merge-strategies/execution.json) |
| Dateutil | Protected-path candidate probe received binary reward 1 in Pier with no exception and missing final CTRF | [Raw-evidence annotation](evidence/pilot/dateutil-rfc5545-timezone-interop/audit-annotation.json) |
| fd | Protected-path candidate probe received binary reward 1 in Pier with no exception and missing final CTRF | [Raw-evidence annotation](evidence/pilot/fd-deterministic-multi-key-sorting/audit-annotation.json) |

The frozen audit parser classifies missing CTRF as invalid execution output and labels Dateutil/fd INFRASTRUCTURE_FAILURE. This label must not hide native reward acceptance of the candidate-only probes. Separate annotations preserve both facts. Their captured stdout lacks write markers, so exact modified targets are not individually confirmed from logs.

Unreached attack probes are unresolved evidence, not proof of verifier resistance. KaTeX's registry rate limit is an infrastructure blocker, not a task defect. Raw S0 judgments are model reviews, with discrepancies and contract ambiguities recorded separately; they are not substituted for durable execution evidence.
