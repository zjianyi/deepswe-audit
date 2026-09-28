# DeepSWE 103-task expansion — final audit

All **103 scheduled tasks have recorded static, native and S0 outcomes or supported blockers**. **Zero clean three-phase results.** The audit is complete as evidence collection and accounting; it is not a release approval. The frozen [ten-task pilot](REPORT.md) and its evidence remain unchanged.

| Phase | Outcomes recorded | Resolved PASS/FAIL | PASS | FAIL | Deferred | Infrastructure blocked |
|---|---:|---:|---:|---:|---:|---:|
| Static | 103 | 103 | 87 | 16 | 0 | 0 |
| Native execution | 103 | 56 | 0 | 56 | 26 | 21 |
| S0 semantic review | 103 | 46 | 0 | 46 | 29 | 28 |

Thirty-five tasks have all three phases resolved as PASS or FAIL; every one includes a failure. The other 68 retain at least one deferred or infrastructure-blocked phase. A recorded outcome is not a resolved phase, and a resolved failure is not a clean result.

## Native findings

Of 103 tasks, 82 reached native execution. Every executable oracle/no-op pair returned binary reward **1/0**; legitimate no-op partial credit is preserved. The other 21 tasks were blocked before case execution by the registry: **17 Data limit exceeded, 4 Rate exceeded**. These are not claims that the images do not exist. No native retries were used.

**56 tasks accepted protected-path probe reward 1 through Pier without a trial exception.** Explicit reach and protected-write markers support path attribution for 39; 17 lack those markers, so exact write-path attribution remains unresolved. Raw evidence and separate annotations preserve this distinction. Missing final CTRF does not erase recorded reward acceptance, and accepted reward does not establish a valid solution.

Four of those tasks also accepted forged-report reward 1: `geo-shapeindex-serialization`, `go-critic-doc-link-checker`, `kysely-window-grouping-helpers`, and `participle-grammar-conflict-analysis`. These are overlapping findings, not four additional affected tasks. Forged-report probes use auditor-known hidden test identifiers; this demonstrates report-trust risk, not unaided solver discovery.

The 26 deferred native outcomes have oracle/no-op evidence but insufficient observed attack reach. Rejected attack reward 0 without reach markers does not prove resistance. The five-case suite is not an exhaustive exploit or semantic-mutant campaign.

## Semantic findings and limits

Exactly one local ChatGPT-authenticated, read-only `gpt-5.6-luna` S0 attempt was recorded per task, including native-blocked tasks. **75 outputs validated: 46 FAIL and 29 deferred.** The other **28 failed strict output validation** and remain explicit audit infrastructure blockers. All 103 original raw outputs, attempt markers and input bundles are archived locally; rejected reviews were neither repaired nor repeated.

Semantic findings include corroborated evaluator-integrity failures and static contract/coverage concerns. They are reviewer findings, not automatically demonstrated task defects. Separate hash-bound annotations reconcile disagreements with native evidence and qualify contract interpretations. For example, True Myth traverse has an Iterable contract but ReadonlyArray signatures, while its runtime uses for-of; the annotation distinguishes that API gap from an unproven legitimate-candidate rejection. Koota and Oxvg annotations similarly preserve interpretation limits. Original S0 outputs are unchanged.

Runtime image digests are recorded where execution reached image resolution. Static mutable-build-image warnings, independent-solution calibration, unobserved probe reach and other deferred criteria remain unresolved. Declared resources and capacity preflight do not measure peak usage or establish a hard storage quota. Inert pinned source context does not prove absence of hidden image-layer or Git-history assets.

## Scope and provenance

The exact [103-task cohort](manifests/expansion.json) is the complement of the frozen ten-task pilot at upstream `0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea`, using Pier `0.3.1` at `df89f994623a0a6a57229103b6fe910766693c30`. [Native run 36363797336](https://github.com/zjianyi/deepswe-audit/actions/runs/36363797336) used driver `e0f63ae14f4fbd4ad74d615372ec720f3609b33c`; all 103 serial matrix jobs and setup completed. Workflow success means the evidence-producing jobs completed, not that QC passed.

Native and authenticated S0 work each ran at concurrency one. The audit retained frozen task bytes, first attempts, declared two-CPU/8-GiB RAM/20-GiB storage settings and recorded preflight checks. No upstream repair, task replacement, paid model-solving trial, API fallback, extra S0 review or native retry was performed. Private BTQC source/rubric/validation and Banana Bench Task 001 were not changed.

Expansion-only capture records Pier reward acceptance even without CTRF and archives S0 raw output before validation. These changes do not alter the frozen private rubric or overwrite pilot evidence. Findings describe this frozen cohort and observed diagnostic probes; they do not establish behavior under every candidate or environment.

## Evidence and verification

- [Final run manifest](manifests/expansion-run.json): pins, task/context hashes, per-case rewards, native artifact hashes and local raw-review archive hashes.
- [Final completion accounting](evidence/expansion-summary.json): per-task recorded, resolved and clean states.
- [Independent S0 accounting](evidence/expansion-accounting-final.json): **2,238 checks**, no discrepancies; 103 attempt/raw/input/bundle/public/local bindings and 75 S0-only ledgers.
- Independent native reconciliation verified **7,680/7,680 artifact hashes across all 103 tasks**, including public/native bindings and case outcomes. Batch records are linked by hash in the final run manifest.
- Final local checks: **27 public tests passed**, all **103 frozen task hashes**, **48 frozen framework file hashes**, **103 context hashes**, and **339 public evidence hashes** verified. The pilot report and 25 public pilot evidence files remain byte-identical to the driver commit.
- Detailed source, native and raw review/input bundles remain local. GitHub native artifacts have 30-day retention; local archives preserve their hashes and evidence.

## Per-task outcomes

| Language | Task | Static | Native | S0 |
|---|---|---|---|---|
| go | [abs-module-cache-flags](evidence/expansion/abs-module-cache-flags) | PASS | FAIL | FAIL |
| go | [abs-stepped-slices](evidence/expansion/abs-stepped-slices) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | [actionlint-action-pinning-lint](evidence/expansion/actionlint-action-pinning-lint) | PASS | FAIL | FAIL |
| python | [adaptix-name-mapping-aliases](evidence/expansion/adaptix-name-mapping-aliases) | PASS | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| python | [aiomonitor-task-snapshots-diff](evidence/expansion/aiomonitor-task-snapshots-diff) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | [anko-default-function-arguments](evidence/expansion/anko-default-function-arguments) | PASS | FAIL | FAIL |
| go | [anko-typed-variable-bindings](evidence/expansion/anko-typed-variable-bindings) | PASS | FAIL | FAIL |
| go | [arcane-drift-detection-baselines](evidence/expansion/arcane-drift-detection-baselines) | PASS | FAIL | FAIL |
| typescript | [arktype-json-schema-refs-dependencies](evidence/expansion/arktype-json-schema-refs-dependencies) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| python | [bandit-incremental-cache-control](evidence/expansion/bandit-incremental-cache-control) | FAIL | FAIL | FAIL |
| python | [bandit-interprocedural-taint-checks](evidence/expansion/bandit-interprocedural-taint-checks) | PASS | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| rust | [boa-hierarchical-evaluation-cancellation](evidence/expansion/boa-hierarchical-evaluation-cancellation) | PASS | INFRASTRUCTURE_FAILURE | INFRASTRUCTURE_FAILURE |
| python | [cattrs-partial-structuring-recovery](evidence/expansion/cattrs-partial-structuring-recovery) | FAIL | INFRASTRUCTURE_FAILURE | FAIL |
| typescript | [clack-async-autocomplete-options](evidence/expansion/clack-async-autocomplete-options) | PASS | INFRASTRUCTURE_FAILURE | FAIL |
| typescript | [claude-code-by-agents-recursive-delegation](evidence/expansion/claude-code-by-agents-recursive-delegation) | PASS | DEFERRED_EVIDENCE_REQUIRED | INFRASTRUCTURE_FAILURE |
| typescript | [cliffy-config-file-parsing](evidence/expansion/cliffy-config-file-parsing) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| javascript | [csstree-shorthand-expansion-compression](evidence/expansion/csstree-shorthand-expansion-compression) | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| go | [dasel-html-document-format](evidence/expansion/dasel-html-document-format) | PASS | FAIL | FAIL |
| typescript | [drizzle-orm-window-function-builders](evidence/expansion/drizzle-orm-window-function-builders) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [dynamodb-toolbox-conditional-attribute-requirements](evidence/expansion/dynamodb-toolbox-conditional-attribute-requirements) | PASS | FAIL | FAIL |
| typescript | [dynamodb-toolbox-lazy-recursive-schemas](evidence/expansion/dynamodb-toolbox-lazy-recursive-schemas) | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [effect-sse-httpapi-streaming](evidence/expansion/effect-sse-httpapi-streaming) | PASS | INFRASTRUCTURE_FAILURE | INFRASTRUCTURE_FAILURE |
| typescript | [eicrud-keyset-pagination-cursor](evidence/expansion/eicrud-keyset-pagination-cursor) | PASS | INFRASTRUCTURE_FAILURE | FAIL |
| go | [etree-xml-diff-patch](evidence/expansion/etree-xml-diff-patch) | PASS | FAIL | FAIL |
| go | [expr-try-catch-errors](evidence/expansion/expr-try-catch-errors) | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| python | [fastapi-deprecation-response-headers](evidence/expansion/fastapi-deprecation-response-headers) | PASS | INFRASTRUCTURE_FAILURE | INFRASTRUCTURE_FAILURE |
| python | [fastapi-implicit-head-options](evidence/expansion/fastapi-implicit-head-options) | PASS | FAIL | FAIL |
| go | [geo-shapeindex-serialization](evidence/expansion/geo-shapeindex-serialization) | PASS | FAIL | FAIL |
| go | [go-critic-doc-link-checker](evidence/expansion/go-critic-doc-link-checker) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | [go-genai-streamed-function-args](evidence/expansion/go-genai-streamed-function-args) | PASS | FAIL | FAIL |
| go | [go-git-worktree-merge-conflicts](evidence/expansion/go-git-worktree-merge-conflicts) | PASS | FAIL | FAIL |
| python | [gql-incremental-graphql-delivery](evidence/expansion/gql-incremental-graphql-delivery) | FAIL | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [happy-dom-deterministic-intersectionobserver](evidence/expansion/happy-dom-deterministic-intersectionobserver) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| go | [helm-unified-manifest-stream](evidence/expansion/helm-unified-manifest-stream) | PASS | FAIL | FAIL |
| typescript | [httpx-deterministic-cookie-store](evidence/expansion/httpx-deterministic-cookie-store) | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| python | [httpx-multipart-response-parsing](evidence/expansion/httpx-multipart-response-parsing) | PASS | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| python | [httpx-streaming-json-iteration](evidence/expansion/httpx-streaming-json-iteration) | PASS | FAIL | FAIL |
| python | [igel-persist-feature-schema](evidence/expansion/igel-persist-feature-schema) | PASS | FAIL | FAIL |
| typescript | [ink-grid-box-layout](evidence/expansion/ink-grid-box-layout) | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| python | [ipython-session-bundle-replay](evidence/expansion/ipython-session-bundle-replay) | PASS | FAIL | FAIL |
| go | [kcp-go-multiplexed-kcp-streams](evidence/expansion/kcp-go-multiplexed-kcp-streams) | PASS | FAIL | FAIL |
| typescript | [kea-atomic-signal-selectors](evidence/expansion/kea-atomic-signal-selectors) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| go | [kgateway-consistent-hash-policy](evidence/expansion/kgateway-consistent-hash-policy) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| python | [kombu-single-active-consumer-priority](evidence/expansion/kombu-single-active-consumer-priority) | PASS | FAIL | FAIL |
| python | [kombu-virtual-queue-dead-lettering](evidence/expansion/kombu-virtual-queue-dead-lettering) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| typescript | [koota-composite-trait-aspects](evidence/expansion/koota-composite-trait-aspects) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [koota-deferred-mutation-buffer](evidence/expansion/koota-deferred-mutation-buffer) | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| python | [koota-entity-snapshot-rollback](evidence/expansion/koota-entity-snapshot-rollback) | PASS | DEFERRED_EVIDENCE_REQUIRED | INFRASTRUCTURE_FAILURE |
| typescript | [koota-pair-relation-tracking](evidence/expansion/koota-pair-relation-tracking) | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| typescript | [koota-query-predicates](evidence/expansion/koota-query-predicates) | PASS | DEFERRED_EVIDENCE_REQUIRED | INFRASTRUCTURE_FAILURE |
| typescript | [kysely-window-grouping-helpers](evidence/expansion/kysely-window-grouping-helpers) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| python | [langchain-request-coalescing](evidence/expansion/langchain-request-coalescing) | FAIL | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| python | [mashumaro-flattened-dataclass-fields](evidence/expansion/mashumaro-flattened-dataclass-fields) | FAIL | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [meriyah-explicit-resource-declarations](evidence/expansion/meriyah-explicit-resource-declarations) | PASS | FAIL | FAIL |
| python | [mnamer-daemon-watch-lifecycle](evidence/expansion/mnamer-daemon-watch-lifecycle) | PASS | FAIL | FAIL |
| python | [mobly-grouped-test-barriers](evidence/expansion/mobly-grouped-test-barriers) | FAIL | FAIL | FAIL |
| python | [narwhals-rolling-window-suite](evidence/expansion/narwhals-rolling-window-suite) | FAIL | INFRASTRUCTURE_FAILURE | FAIL |
| python | [numba-stencil-boundary-modes](evidence/expansion/numba-stencil-boundary-modes) | FAIL | FAIL | INFRASTRUCTURE_FAILURE |
| typescript | [obsidian-linter-auto-table-of-contents](evidence/expansion/obsidian-linter-auto-table-of-contents) | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| typescript | [obsidian-linter-link-format-conversion](evidence/expansion/obsidian-linter-link-format-conversion) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [obsidian-linter-scoped-ignore-markers](evidence/expansion/obsidian-linter-scoped-ignore-markers) | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [ofetch-per-origin-circuit-breaker](evidence/expansion/ofetch-per-origin-circuit-breaker) | PASS | FAIL | FAIL |
| go | [onedump-dump-encryption-pipeline](evidence/expansion/onedump-dump-encryption-pipeline) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | [opa-rego-rule-profiling](evidence/expansion/opa-rego-rule-profiling) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | [opa-template-string-reconstruction](evidence/expansion/opa-template-string-reconstruction) | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [optique-conditional-option-dependencies](evidence/expansion/optique-conditional-option-dependencies) | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| rust | [oxvg-structural-selector-preservation](evidence/expansion/oxvg-structural-selector-preservation) | PASS | INFRASTRUCTURE_FAILURE | FAIL |
| go | [participle-grammar-conflict-analysis](evidence/expansion/participle-grammar-conflict-analysis) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | [pebble-durability-wait-apis](evidence/expansion/pebble-durability-wait-apis) | PASS | FAIL | FAIL |
| rust | [pest-character-class-coalescing](evidence/expansion/pest-character-class-coalescing) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [prometheus-transactional-reload-status](evidence/expansion/prometheus-transactional-reload-status) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| go | [prometheus-typed-label-sorting](evidence/expansion/prometheus-typed-label-sorting) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| python | [psd-tools-blend-range-api](evidence/expansion/psd-tools-blend-range-api) | FAIL | FAIL | INFRASTRUCTURE_FAILURE |
| python | [pwntools-tube-multiplexing](evidence/expansion/pwntools-tube-multiplexing) | FAIL | FAIL | FAIL |
| python | [python-statemachine-state-data-scoping](evidence/expansion/python-statemachine-state-data-scoping) | FAIL | FAIL | INFRASTRUCTURE_FAILURE |
| typescript | [query-persist-restored-query-state](evidence/expansion/query-persist-restored-query-state) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [quill-shared-toolbar-focus](evidence/expansion/quill-shared-toolbar-focus) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| python | [returns-validated-error-accumulation](evidence/expansion/returns-validated-error-accumulation) | FAIL | FAIL | FAIL |
| go | [scc-bounded-memory-spilling](evidence/expansion/scc-bounded-memory-spilling) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | [scriggo-method-declarations](evidence/expansion/scriggo-method-declarations) | PASS | FAIL | FAIL |
| python | [skrub-duration-encoding](evidence/expansion/skrub-duration-encoding) | FAIL | FAIL | FAIL |
| typescript | [sql-formatter-bigquery-pipe-formatting](evidence/expansion/sql-formatter-bigquery-pipe-formatting) | PASS | DEFERRED_EVIDENCE_REQUIRED | INFRASTRUCTURE_FAILURE |
| python | [sqlfmt-create-table-ddl-formatting](evidence/expansion/sqlfmt-create-table-ddl-formatting) | FAIL | FAIL | INFRASTRUCTURE_FAILURE |
| python | [sqlite-utils-safe-import-checkpoints](evidence/expansion/sqlite-utils-safe-import-checkpoints) | FAIL | FAIL | FAIL |
| typescript | [superjson-error-stack-serialization](evidence/expansion/superjson-error-stack-serialization) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| go | [task-task-graph-export](evidence/expansion/task-task-graph-export) | PASS | INFRASTRUCTURE_FAILURE | INFRASTRUCTURE_FAILURE |
| go | [tengo-callable-instance-isolation](evidence/expansion/tengo-callable-instance-isolation) | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| go | [tengo-destructuring-bindings](evidence/expansion/tengo-destructuring-bindings) | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| go | [termenv-preserve-ansi-resets](evidence/expansion/termenv-preserve-ansi-resets) | PASS | INFRASTRUCTURE_FAILURE | FAIL |
| javascript | [testem-per-launcher-reports](evidence/expansion/testem-per-launcher-reports) | PASS | INFRASTRUCTURE_FAILURE | INFRASTRUCTURE_FAILURE |
| python | [textual-kitty-key-phases](evidence/expansion/textual-kitty-key-phases) | PASS | FAIL | FAIL |
| python | [textual-richlog-follow-state](evidence/expansion/textual-richlog-follow-state) | FAIL | FAIL | FAIL |
| python | [tomlkit-toml-table-converters](evidence/expansion/tomlkit-toml-table-converters) | PASS | FAIL | FAIL |
| typescript | [true-myth-iterable-collection-combinators](evidence/expansion/true-myth-iterable-collection-combinators) | PASS | FAIL | FAIL |
| typescript | [ts-pattern-match-each](evidence/expansion/ts-pattern-match-each) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| go | [updo-policy-alerting](evidence/expansion/updo-policy-alerting) | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| typescript | [valibot-recursive-schema-composition](evidence/expansion/valibot-recursive-schema-composition) | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | [vitest-duration-sharding](evidence/expansion/vitest-duration-sharding) | PASS | DEFERRED_EVIDENCE_REQUIRED | INFRASTRUCTURE_FAILURE |
| python | [vulture-persistent-analysis-cache](evidence/expansion/vulture-persistent-analysis-cache) | PASS | FAIL | FAIL |
| go | [wazero-multi-module-snapshots](evidence/expansion/wazero-multi-module-snapshots) | PASS | INFRASTRUCTURE_FAILURE | INFRASTRUCTURE_FAILURE |
| go | [yaegi-go-embed-directives](evidence/expansion/yaegi-go-embed-directives) | PASS | FAIL | FAIL |
| javascript | [yjs-map-conflict-detection](evidence/expansion/yjs-map-conflict-detection) | PASS | DEFERRED_EVIDENCE_REQUIRED | INFRASTRUCTURE_FAILURE |
| go | [ytt-jsonpath-query-api](evidence/expansion/ytt-jsonpath-query-api) | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
