# DeepSWE three-phase QC audit

Audit of Datacurve DeepSWE at `0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea`, using Pier 0.3.1. This repository contains newly authored audit code, a frozen 113-task inventory, a fixed ten-task pilot, and evidence summaries. It does not distribute the private BTQC framework or duplicate the upstream task corpus.

The local BTQC integration performs static and semantic review. Public GitHub jobs run only the public native driver and locked Pier dependencies. Semantic review uses local ChatGPT-authenticated Codex, default `gpt-5.6-luna`, with inert source text and no API fallback.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/inventory.py --source /path/to/pinned/deep-swe
# On qualifying Linux, with locked dependencies installed:
uv run python scripts/native_runner.py --task goreleaser-retry-publish-auditing --source /path/to/pinned/deep-swe --output /fresh/evidence/path
```

GitHub workflow `pilot.yml` has `smoke` and `remaining` cohorts. Run and validate smoke evidence before the remaining cohort. Each task runs sequentially through oracle, nop, and three candidate-only probes in fresh containers. An unreached probe is deferred, never evidence of resistance. Missing or invalid infrastructure is not a model failure.

See `manifests/frozen.json` for the complete deterministic selection and task hashes, `docs/DECISIONS.md` for policy, and `docs/STATE.md` for current progress. The [final report](REPORT.md) distinguishes task defects, unresolved evidence, and infrastructure blockers. All scheduled outcomes are recorded; zero tasks have a clean three-phase result. See [the run manifest](manifests/run.json) for hashes and [public completion accounting](evidence/audit-summary.json) for phase status. This balanced pilot is not an unbiased estimate of corpus-wide defect prevalence.

The user-authorized [103-task expansion](EXPANSION.md) runs separately using `expansion.yml` and `manifests/expansion.json`. The original pilot results remain frozen.
