# DeepSWE audit report

Frozen upstream `0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea`. Corpus: 113 tasks. Pilot: ten tasks across five languages and ten repositories.

Static outcomes: `{'FAIL': 16, 'PASS': 97}`.

| Task | Static | Execution | Semantic | Clean three-phase |
|---|---|---|---|---|
| goreleaser-retry-publish-auditing | PASS | FAIL | DEFERRED_EVIDENCE_REQUIRED | False |
| helm-array-merge-strategies | PASS | FAIL | FAIL | False |
| testem-bail-on-test-failure | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED | False |
| katex-multicolumn-array-spans | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED | False |
| bandit-structured-nosec-directives | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL | False |
| dateutil-rfc5545-timezone-interop | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED | False |
| fd-deterministic-multi-key-sorting | PASS | INFRASTRUCTURE_FAILURE | FAIL | False |
| wasmi-trap-coredumps | PASS | DEFERRED_EVIDENCE_REQUIRED | NOT_RUN | False |
| awilix-async-container-initialization | PASS | DEFERRED_EVIDENCE_REQUIRED | NOT_RUN | False |
| happy-dom-abort-pending-body-reads | PASS | DEFERRED_EVIDENCE_REQUIRED | NOT_RUN | False |

## Interpretation

Task failures, unresolved evidence, and infrastructure failures are reported separately. An explicit blocker accounts for a scheduled item but does not mean the phase evaluated the task. This balanced pilot is not an unbiased corpus-wide defect-rate estimate.

Detailed findings are under `evidence/pilot/<task>/semantic.json`; native summaries are adjacent. Public GitHub artifacts retain raw native evidence for 30 days; a local copy is preserved under `.local/native`.
