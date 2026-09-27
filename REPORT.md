# DeepSWE audit report

Frozen upstream `0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea`. Corpus: 113 tasks. Pilot: ten tasks across five languages and ten repositories.

Static outcomes: `{'FAIL': 16, 'PASS': 97}`.

| Task | Static | Execution | Semantic | Clean three-phase |
|---|---|---|---|---|
| goreleaser-retry-publish-auditing | PASS | FAIL | DEFERRED_EVIDENCE_REQUIRED | False |
| helm-array-merge-strategies | PASS | NOT_RUN | NOT_RUN | False |
| testem-bail-on-test-failure | PASS | NOT_RUN | NOT_RUN | False |
| katex-multicolumn-array-spans | PASS | NOT_RUN | NOT_RUN | False |
| bandit-structured-nosec-directives | PASS | NOT_RUN | NOT_RUN | False |
| dateutil-rfc5545-timezone-interop | PASS | NOT_RUN | NOT_RUN | False |
| fd-deterministic-multi-key-sorting | PASS | NOT_RUN | NOT_RUN | False |
| wasmi-trap-coredumps | PASS | NOT_RUN | NOT_RUN | False |
| awilix-async-container-initialization | PASS | NOT_RUN | NOT_RUN | False |
| happy-dom-abort-pending-body-reads | PASS | NOT_RUN | NOT_RUN | False |

## Interpretation

Task failures, unresolved evidence, and infrastructure failures are reported separately. An explicit blocker accounts for a scheduled item but does not mean the phase evaluated the task. This balanced pilot is not an unbiased corpus-wide defect-rate estimate.

Detailed findings are under `evidence/pilot/<task>/semantic.json`; native summaries are adjacent. Public GitHub artifacts retain raw native evidence for 30 days; a local copy is preserved under `.local/native`.
