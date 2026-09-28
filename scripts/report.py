"""Reproduce public audit accounting without private BTQC or task source."""
from pathlib import Path
import collections
import json
from audit_core import UPSTREAM, write, sha

ROOT = Path(__file__).resolve().parents[1]
TERMINAL = {'PASS', 'FAIL'}


def accounting(phases):
    return {
        'all_outcomes_recorded': len(phases) == 3 and all(v != 'NOT_RUN' for v in phases.values()),
        'all_phases_resolved': len(phases) == 3 and all(v in TERMINAL for v in phases.values()),
        'clean_three_phase_result': len(phases) == 3 and all(v == 'PASS' for v in phases.values()),
    }


def report(root=ROOT):
    read = lambda p: json.loads((root / p).read_text())
    frozen = read('manifests/frozen.json')
    static = read('evidence/static-summary.json')
    rows = []
    for task_id in frozen['pilot']:
        s = next(r for r in static['tasks'] if r['task_id'] == task_id)
        prefix = Path('evidence/pilot') / task_id
        ep, sp, ap = (root / prefix / n for n in ('execution.json', 'semantic.json', 'audit-annotation.json'))
        e = json.loads(ep.read_text()) if ep.exists() else {}
        m = json.loads(sp.read_text()) if sp.exists() else {}
        a = json.loads(ap.read_text()) if ap.exists() else {}
        phases = {'static': s['status'], 'execution': e.get('status', 'NOT_RUN'), 'semantic': m.get('overall_status', 'NOT_RUN')}
        concrete = a.get('finding') == 'CANDIDATE_REWARD_FORGERY_ACCEPTED_BY_PIER' or any(c.get('protected_write_observed') for c in e.get('cases', {}).values())
        rows.append({'task_id': task_id, 'language': s['language'], 'repository': s['repository'], 'phases': phases,
                     **accounting(phases), 'demonstrated_integrity_finding': concrete,
                     'semantic_finding_count': len(m.get('findings', [])),
                     'evidence_hashes': {p.name: sha(p) for p in (ep, sp, ap) if p.exists()}})
    summary = {'schema_version': 'deepswe.audit-summary/2', 'upstream_commit': UPSTREAM,
               'frozen_manifest_hash': frozen['manifest_hash'], 'corpus_static_counts': static['counts'], 'pilot': rows,
               'recorded_outcome_counts': {p: sum(r['phases'][p] != 'NOT_RUN' for r in rows) for p in ('static','execution','semantic')},
               'resolved_phase_counts': {p: sum(r['phases'][p] in TERMINAL for r in rows) for p in ('static','execution','semantic')},
               'phase_status_counts': {p: dict(collections.Counter(r['phases'][p] for r in rows)) for p in ('static','execution','semantic')},
               'scheduled_items_accounted': all(r['all_outcomes_recorded'] for r in rows),
               'clean_count': sum(r['clean_three_phase_result'] for r in rows),
               'demonstrated_integrity_finding_count': sum(r['demonstrated_integrity_finding'] for r in rows),
               'claim': 'Balanced pilot; not a corpus prevalence estimate or release approval.'}
    write(root / 'evidence/audit-summary.json', summary)
    labels = {'PASS':'PASS', 'FAIL':'FAIL', 'DEFERRED_EVIDENCE_REQUIRED':'Deferred', 'INFRASTRUCTURE_FAILURE':'Blocked', 'NOT_RUN':'Not run'}
    lines = ['# DeepSWE three-phase QC audit', '',
             f'Frozen upstream `{UPSTREAM}`; Pier `0.3.1`. The inventory covers 113 tasks. The fixed pilot covers ten tasks, two per language and ten repositories.', '',
             'All scheduled items now have a recorded outcome or explicit blocker. This is accounting completion, not a clean audit: **0/10 clean three-phase results**.', '',
             'Static checks returned **97 PASS / 16 FAIL**, with reproducibility warnings across all 113 tasks. The 16 failures concern unpinned Python package installation; file/line evidence is in [the static inventory](evidence/static-summary.json). All ten pilot tasks passed static checks with warnings.', '',
             '**Execution:** nine oracle/no-op pairs returned the expected binary rewards 1/0. KaTeX never reached execution because its image pull was rate-limited. No-op partial credit remained native and was not required to be zero. All 50 scheduled cases are accounted for: 45 ran, five were blocked before execution.', '',
             '**Semantic:** ten S0 attempts through local ChatGPT-authenticated `gpt-5.6-luna`, read-only, with no API fallback. Nine produced validated reviews (three FAIL, six deferred); Happy DOM returned an invalid structured review and remains blocked. No S0 was rerun.', '',
             '| Language | Task / repository | Execution (frozen importer) | S0 | Demonstrated integrity finding |',
             '|---|---|---|---|---|']
    for r in rows:
        task = r['task_id']; repo = r['repository'].removesuffix('.git').split('/')[-1]
        lines.append(f"| {r['language']} | [{task}](evidence/pilot/{task}/execution.json) / {repo} | {labels.get(r['phases']['execution'],r['phases']['execution'])} | {labels.get(r['phases']['semantic'],r['phases']['semantic'])} | {'Yes' if r['demonstrated_integrity_finding'] else 'Not established'} |")
    lines += ['', '## Concrete findings', '',
              '- **Dateutil and fd:** the candidate-only protected-path attack received binary reward **1** in Pier with no exception despite missing final CTRF. The attack contained no feature implementation. Durable reward files and native trial results support this conclusion. See the [Dateutil](evidence/pilot/dateutil-rfc5545-timezone-interop/audit-annotation.json) and [fd](evidence/pilot/fd-deterministic-multi-key-sorting/audit-annotation.json) annotations and artifact hashes.',
              '- **GoReleaser and Helm:** candidate code wrote protected verifier surfaces and disrupted grading. Report-forgery probes inflated native partial credit from **0.5 to 0.982759** and **0.203390 to 0.813559**, respectively; binary rewards stayed zero.', '',
              'The frozen importer labels Dateutil/fd as infrastructure failures because final reports are missing. That correctly prevents credit as valid task solutions, but hides native reward acceptance in its aggregate label. Separate annotations retain the demonstrated exploit alongside the immutable importer output. Empty captured logs prevent identification of every successfully written target; no stdout-marker absence is treated as proof of nonexecution.', '',
              '## Review findings and limitations', '',
              'The S0 FAIL reviews flag Helm mixed-array ordering, Bandit verifier integrity, and fd random-sort/timestamp coverage. These are reviewer findings, not all independently demonstrated defects: Helm ordering involves contract interpretation, and Bandit’s generic attacks did not provide reach evidence. GoReleaser’s S0 incorrectly described protected writes as rejected; Helm’s S0 incorrectly claimed execution evidence was absent. Their original reviews remain intact with separate annotations.', '',
              'Unobserved attack markers leave resistance unresolved. Forged-report payloads were constructed with auditor knowledge of hidden test IDs, so they demonstrate a reachable report-trust weakness rather than an unaided solver discovery. Protected-path reward bypasses do not depend on guessing those IDs. The probe suite is not an exhaustive exploit or semantic-mutant campaign.', '',
              'Runtime image digests were resolved for nine tasks. The audit retained declared two-CPU, 8-GiB RAM, 20-GiB storage and verifier network/timeout settings and recorded Linux/AMD64, memory and disk preflight. Preflight capacity is not a measurement of peak usage or proof of a hard storage quota. Image-layer hidden assets and future Git-history exposure remain incompletely corroborated at runtime; static Dockerfile inspection and pinned source excerpts do not establish their absence.', '',
              'KaTeX is blocked by `toomanyrequests: Rate exceeded`, not a confirmed missing image. No documented correction was established, so no retry was used. Happy DOM is blocked by `REVIEW_OUTPUT_INVALID`: conflicting SEM-020 findings failed strict local validation. Its prepared input and validation errors are retained; the private reviewer did not retain the rejected raw output after temporary-directory cleanup. This is an audit-tool evidence limitation, not a task defect.', '',
              'No upstream repairs, model-solving trials, paid API fallback, extra mutants, repeated successful runs, or sample replacement were performed. Findings from this deliberately balanced pilot must not be interpreted as an unbiased defect-rate estimate for the 113-task corpus.', '',
              '## Reproduction and evidence', '',
              '- [Frozen inventory and selection](manifests/frozen.json), [private framework/context hashes](manifests/qc-snapshot.json), and [run manifest](manifests/run.json).',
              '- [Machine-readable completion accounting](evidence/audit-summary.json) distinguishes recorded outcomes from resolved phases; deferred, blocked and human-review outcomes cannot be clean.',
              '- [Smoke run](https://github.com/zjianyi/deepswe-audit/actions/runs/36353718484) and [remaining nine](https://github.com/zjianyi/deepswe-audit/actions/runs/36356902711). Public raw native artifacts have 30-day retention; downloaded bundles and inert source/review inputs are retained locally.',
              '- Regenerate this report and summary with `python3 scripts/report.py`. Public runner reproduction uses the locked environment and `scripts/native_runner.py`; private BTQC is needed only for local normalization/review, never public jobs.', '',
              'Validation: 112 BTQC regression tests and 17 public runner fixtures passed before corpus execution. Final validation passed all 19 public tests (including completion-accounting checks), all native artifact bindings, all 113 frozen task hashes, framework/context hashes and one S0 attempt per task. Workflow validation passed. Detailed source bundles remain local; BTQC remains private.', '']
    (root / 'REPORT.md').write_text('\n'.join(lines))
    return summary


if __name__ == '__main__':
    print(report()['recorded_outcome_counts'])
