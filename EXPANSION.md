# DeepSWE 103-task expansion

User-authorized extension of the frozen ten-task pilot. The original [pilot report](REPORT.md) and evidence remain unchanged.

Recorded outcomes: {'static': 103, 'execution': 75, 'semantic': 75}. Clean three-phase results: 0. Recorded blockers and deferred outcomes are not clean results.

Same upstream/Pier pins, resources, five native cases, 20 semantic criteria and local ChatGPT-authenticated reviewer. One native job and one S0 review at a time. All 103 tasks retain their original denominator; no substitution or automatic retry.

Expansion-only evidence improvements retain native reward acceptance when CTRF is absent and archive raw S0 output before validation. These changes do not repair upstream or alter the rubric. Attack reach and grading risks remain explicitly unresolved where evidence is missing.

| Language | Task | Static | Execution | Semantic |
|---|---|---|---|---|
| go | abs-module-cache-flags | PASS | FAIL | FAIL |
| go | abs-stepped-slices | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | actionlint-action-pinning-lint | PASS | FAIL | FAIL |
| python | adaptix-name-mapping-aliases | PASS | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| python | aiomonitor-task-snapshots-diff | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | anko-default-function-arguments | PASS | FAIL | FAIL |
| go | anko-typed-variable-bindings | PASS | FAIL | FAIL |
| go | arcane-drift-detection-baselines | PASS | FAIL | FAIL |
| typescript | arktype-json-schema-refs-dependencies | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| python | bandit-incremental-cache-control | FAIL | FAIL | FAIL |
| python | bandit-interprocedural-taint-checks | PASS | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| rust | boa-hierarchical-evaluation-cancellation | PASS | INFRASTRUCTURE_FAILURE | INFRASTRUCTURE_FAILURE |
| python | cattrs-partial-structuring-recovery | FAIL | INFRASTRUCTURE_FAILURE | FAIL |
| typescript | clack-async-autocomplete-options | PASS | INFRASTRUCTURE_FAILURE | FAIL |
| typescript | claude-code-by-agents-recursive-delegation | PASS | DEFERRED_EVIDENCE_REQUIRED | INFRASTRUCTURE_FAILURE |
| typescript | cliffy-config-file-parsing | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| javascript | csstree-shorthand-expansion-compression | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| go | dasel-html-document-format | PASS | FAIL | FAIL |
| typescript | drizzle-orm-window-function-builders | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | dynamodb-toolbox-conditional-attribute-requirements | PASS | FAIL | FAIL |
| typescript | dynamodb-toolbox-lazy-recursive-schemas | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| typescript | effect-sse-httpapi-streaming | PASS | INFRASTRUCTURE_FAILURE | INFRASTRUCTURE_FAILURE |
| typescript | eicrud-keyset-pagination-cursor | PASS | INFRASTRUCTURE_FAILURE | FAIL |
| go | etree-xml-diff-patch | PASS | FAIL | FAIL |
| go | expr-try-catch-errors | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| python | fastapi-deprecation-response-headers | PASS | INFRASTRUCTURE_FAILURE | INFRASTRUCTURE_FAILURE |
| python | fastapi-implicit-head-options | PASS | FAIL | FAIL |
| go | geo-shapeindex-serialization | PASS | FAIL | FAIL |
| go | go-critic-doc-link-checker | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | go-genai-streamed-function-args | PASS | FAIL | FAIL |
| go | go-git-worktree-merge-conflicts | PASS | FAIL | FAIL |
| python | gql-incremental-graphql-delivery | FAIL | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| typescript | happy-dom-deterministic-intersectionobserver | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| go | helm-unified-manifest-stream | PASS | FAIL | FAIL |
| typescript | httpx-deterministic-cookie-store | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| python | httpx-multipart-response-parsing | PASS | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| python | httpx-streaming-json-iteration | PASS | FAIL | FAIL |
| python | igel-persist-feature-schema | PASS | FAIL | FAIL |
| typescript | ink-grid-box-layout | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| python | ipython-session-bundle-replay | PASS | FAIL | FAIL |
| go | kcp-go-multiplexed-kcp-streams | PASS | FAIL | FAIL |
| typescript | kea-atomic-signal-selectors | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| go | kgateway-consistent-hash-policy | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| python | kombu-single-active-consumer-priority | PASS | FAIL | FAIL |
| python | kombu-virtual-queue-dead-lettering | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| typescript | koota-composite-trait-aspects | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | koota-deferred-mutation-buffer | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| python | koota-entity-snapshot-rollback | PASS | DEFERRED_EVIDENCE_REQUIRED | INFRASTRUCTURE_FAILURE |
| typescript | koota-pair-relation-tracking | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| typescript | koota-query-predicates | PASS | DEFERRED_EVIDENCE_REQUIRED | INFRASTRUCTURE_FAILURE |
| typescript | kysely-window-grouping-helpers | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| python | langchain-request-coalescing | FAIL | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| python | mashumaro-flattened-dataclass-fields | FAIL | FAIL | DEFERRED_EVIDENCE_REQUIRED |
| typescript | meriyah-explicit-resource-declarations | PASS | FAIL | FAIL |
| python | mnamer-daemon-watch-lifecycle | PASS | FAIL | FAIL |
| python | mobly-grouped-test-barriers | FAIL | FAIL | FAIL |
| python | narwhals-rolling-window-suite | FAIL | INFRASTRUCTURE_FAILURE | FAIL |
| python | numba-stencil-boundary-modes | FAIL | FAIL | INFRASTRUCTURE_FAILURE |
| typescript | obsidian-linter-auto-table-of-contents | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| typescript | obsidian-linter-link-format-conversion | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | obsidian-linter-scoped-ignore-markers | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| typescript | ofetch-per-origin-circuit-breaker | PASS | FAIL | FAIL |
| go | onedump-dump-encryption-pipeline | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | opa-rego-rule-profiling | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | opa-template-string-reconstruction | PASS | INFRASTRUCTURE_FAILURE | DEFERRED_EVIDENCE_REQUIRED |
| typescript | optique-conditional-option-dependencies | PASS | DEFERRED_EVIDENCE_REQUIRED | FAIL |
| rust | oxvg-structural-selector-preservation | PASS | INFRASTRUCTURE_FAILURE | FAIL |
| go | participle-grammar-conflict-analysis | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| go | pebble-durability-wait-apis | PASS | FAIL | FAIL |
| rust | pest-character-class-coalescing | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| typescript | prometheus-transactional-reload-status | PASS | DEFERRED_EVIDENCE_REQUIRED | DEFERRED_EVIDENCE_REQUIRED |
| go | prometheus-typed-label-sorting | PASS | FAIL | INFRASTRUCTURE_FAILURE |
| python | psd-tools-blend-range-api | FAIL | FAIL | INFRASTRUCTURE_FAILURE |
| python | pwntools-tube-multiplexing | FAIL | FAIL | FAIL |
| python | python-statemachine-state-data-scoping | FAIL | FAIL | INFRASTRUCTURE_FAILURE |
| typescript | query-persist-restored-query-state | PASS | NOT_RUN | NOT_RUN |
| typescript | quill-shared-toolbar-focus | PASS | NOT_RUN | NOT_RUN |
| python | returns-validated-error-accumulation | FAIL | NOT_RUN | NOT_RUN |
| go | scc-bounded-memory-spilling | PASS | NOT_RUN | NOT_RUN |
| go | scriggo-method-declarations | PASS | NOT_RUN | NOT_RUN |
| python | skrub-duration-encoding | FAIL | NOT_RUN | NOT_RUN |
| typescript | sql-formatter-bigquery-pipe-formatting | PASS | NOT_RUN | NOT_RUN |
| python | sqlfmt-create-table-ddl-formatting | FAIL | NOT_RUN | NOT_RUN |
| python | sqlite-utils-safe-import-checkpoints | FAIL | NOT_RUN | NOT_RUN |
| typescript | superjson-error-stack-serialization | PASS | NOT_RUN | NOT_RUN |
| go | task-task-graph-export | PASS | NOT_RUN | NOT_RUN |
| go | tengo-callable-instance-isolation | PASS | NOT_RUN | NOT_RUN |
| go | tengo-destructuring-bindings | PASS | NOT_RUN | NOT_RUN |
| go | termenv-preserve-ansi-resets | PASS | NOT_RUN | NOT_RUN |
| javascript | testem-per-launcher-reports | PASS | NOT_RUN | NOT_RUN |
| python | textual-kitty-key-phases | PASS | NOT_RUN | NOT_RUN |
| python | textual-richlog-follow-state | FAIL | NOT_RUN | NOT_RUN |
| python | tomlkit-toml-table-converters | PASS | NOT_RUN | NOT_RUN |
| typescript | true-myth-iterable-collection-combinators | PASS | NOT_RUN | NOT_RUN |
| typescript | ts-pattern-match-each | PASS | NOT_RUN | NOT_RUN |
| go | updo-policy-alerting | PASS | NOT_RUN | NOT_RUN |
| typescript | valibot-recursive-schema-composition | PASS | NOT_RUN | NOT_RUN |
| typescript | vitest-duration-sharding | PASS | NOT_RUN | NOT_RUN |
| python | vulture-persistent-analysis-cache | PASS | NOT_RUN | NOT_RUN |
| go | wazero-multi-module-snapshots | PASS | NOT_RUN | NOT_RUN |
| go | yaegi-go-embed-directives | PASS | NOT_RUN | NOT_RUN |
| javascript | yjs-map-conflict-detection | PASS | NOT_RUN | NOT_RUN |
| go | ytt-jsonpath-query-api | PASS | NOT_RUN | NOT_RUN |
