# DeepSWE 103-task expansion

User-authorized extension of the frozen ten-task pilot. The original [pilot report](REPORT.md) and evidence remain unchanged.

Recorded outcomes: {'static': 103, 'execution': 9, 'semantic': 8}. Clean three-phase results: 0. Recorded blockers and deferred outcomes are not clean results.

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
| typescript | arktype-json-schema-refs-dependencies | PASS | DEFERRED_EVIDENCE_REQUIRED | NOT_RUN |
| python | bandit-incremental-cache-control | FAIL | NOT_RUN | NOT_RUN |
| python | bandit-interprocedural-taint-checks | PASS | NOT_RUN | NOT_RUN |
| rust | boa-hierarchical-evaluation-cancellation | PASS | NOT_RUN | NOT_RUN |
| python | cattrs-partial-structuring-recovery | FAIL | NOT_RUN | NOT_RUN |
| typescript | clack-async-autocomplete-options | PASS | NOT_RUN | NOT_RUN |
| typescript | claude-code-by-agents-recursive-delegation | PASS | NOT_RUN | NOT_RUN |
| typescript | cliffy-config-file-parsing | PASS | NOT_RUN | NOT_RUN |
| javascript | csstree-shorthand-expansion-compression | PASS | NOT_RUN | NOT_RUN |
| go | dasel-html-document-format | PASS | NOT_RUN | NOT_RUN |
| typescript | drizzle-orm-window-function-builders | PASS | NOT_RUN | NOT_RUN |
| typescript | dynamodb-toolbox-conditional-attribute-requirements | PASS | NOT_RUN | NOT_RUN |
| typescript | dynamodb-toolbox-lazy-recursive-schemas | PASS | NOT_RUN | NOT_RUN |
| typescript | effect-sse-httpapi-streaming | PASS | NOT_RUN | NOT_RUN |
| typescript | eicrud-keyset-pagination-cursor | PASS | NOT_RUN | NOT_RUN |
| go | etree-xml-diff-patch | PASS | NOT_RUN | NOT_RUN |
| go | expr-try-catch-errors | PASS | NOT_RUN | NOT_RUN |
| python | fastapi-deprecation-response-headers | PASS | NOT_RUN | NOT_RUN |
| python | fastapi-implicit-head-options | PASS | NOT_RUN | NOT_RUN |
| go | geo-shapeindex-serialization | PASS | NOT_RUN | NOT_RUN |
| go | go-critic-doc-link-checker | PASS | NOT_RUN | NOT_RUN |
| go | go-genai-streamed-function-args | PASS | NOT_RUN | NOT_RUN |
| go | go-git-worktree-merge-conflicts | PASS | NOT_RUN | NOT_RUN |
| python | gql-incremental-graphql-delivery | FAIL | NOT_RUN | NOT_RUN |
| typescript | happy-dom-deterministic-intersectionobserver | PASS | NOT_RUN | NOT_RUN |
| go | helm-unified-manifest-stream | PASS | NOT_RUN | NOT_RUN |
| typescript | httpx-deterministic-cookie-store | PASS | NOT_RUN | NOT_RUN |
| python | httpx-multipart-response-parsing | PASS | NOT_RUN | NOT_RUN |
| python | httpx-streaming-json-iteration | PASS | NOT_RUN | NOT_RUN |
| python | igel-persist-feature-schema | PASS | NOT_RUN | NOT_RUN |
| typescript | ink-grid-box-layout | PASS | NOT_RUN | NOT_RUN |
| python | ipython-session-bundle-replay | PASS | NOT_RUN | NOT_RUN |
| go | kcp-go-multiplexed-kcp-streams | PASS | NOT_RUN | NOT_RUN |
| typescript | kea-atomic-signal-selectors | PASS | NOT_RUN | NOT_RUN |
| go | kgateway-consistent-hash-policy | PASS | NOT_RUN | NOT_RUN |
| python | kombu-single-active-consumer-priority | PASS | NOT_RUN | NOT_RUN |
| python | kombu-virtual-queue-dead-lettering | PASS | NOT_RUN | NOT_RUN |
| typescript | koota-composite-trait-aspects | PASS | NOT_RUN | NOT_RUN |
| typescript | koota-deferred-mutation-buffer | PASS | NOT_RUN | NOT_RUN |
| python | koota-entity-snapshot-rollback | PASS | NOT_RUN | NOT_RUN |
| typescript | koota-pair-relation-tracking | PASS | NOT_RUN | NOT_RUN |
| typescript | koota-query-predicates | PASS | NOT_RUN | NOT_RUN |
| typescript | kysely-window-grouping-helpers | PASS | NOT_RUN | NOT_RUN |
| python | langchain-request-coalescing | FAIL | NOT_RUN | NOT_RUN |
| python | mashumaro-flattened-dataclass-fields | FAIL | NOT_RUN | NOT_RUN |
| typescript | meriyah-explicit-resource-declarations | PASS | NOT_RUN | NOT_RUN |
| python | mnamer-daemon-watch-lifecycle | PASS | NOT_RUN | NOT_RUN |
| python | mobly-grouped-test-barriers | FAIL | NOT_RUN | NOT_RUN |
| python | narwhals-rolling-window-suite | FAIL | NOT_RUN | NOT_RUN |
| python | numba-stencil-boundary-modes | FAIL | NOT_RUN | NOT_RUN |
| typescript | obsidian-linter-auto-table-of-contents | PASS | NOT_RUN | NOT_RUN |
| typescript | obsidian-linter-link-format-conversion | PASS | NOT_RUN | NOT_RUN |
| typescript | obsidian-linter-scoped-ignore-markers | PASS | NOT_RUN | NOT_RUN |
| typescript | ofetch-per-origin-circuit-breaker | PASS | NOT_RUN | NOT_RUN |
| go | onedump-dump-encryption-pipeline | PASS | NOT_RUN | NOT_RUN |
| go | opa-rego-rule-profiling | PASS | NOT_RUN | NOT_RUN |
| go | opa-template-string-reconstruction | PASS | NOT_RUN | NOT_RUN |
| typescript | optique-conditional-option-dependencies | PASS | NOT_RUN | NOT_RUN |
| rust | oxvg-structural-selector-preservation | PASS | NOT_RUN | NOT_RUN |
| go | participle-grammar-conflict-analysis | PASS | NOT_RUN | NOT_RUN |
| go | pebble-durability-wait-apis | PASS | NOT_RUN | NOT_RUN |
| rust | pest-character-class-coalescing | PASS | NOT_RUN | NOT_RUN |
| typescript | prometheus-transactional-reload-status | PASS | NOT_RUN | NOT_RUN |
| go | prometheus-typed-label-sorting | PASS | NOT_RUN | NOT_RUN |
| python | psd-tools-blend-range-api | FAIL | NOT_RUN | NOT_RUN |
| python | pwntools-tube-multiplexing | FAIL | NOT_RUN | NOT_RUN |
| python | python-statemachine-state-data-scoping | FAIL | NOT_RUN | NOT_RUN |
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
