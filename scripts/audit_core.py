"""Public, dependency-free DeepSWE provenance and result validation utilities."""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path

UPSTREAM = '0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea'
PIER = '0.3.1'
PIER_COMMIT = 'df89f994623a0a6a57229103b6fe910766693c30'
SEED = 'deepswe-btqc-pilot-v1|' + UPSTREAM
CASES = ('oracle', 'nop', 'suppress-tests', 'forge-reports', 'protected-paths')
PILOT = ['goreleaser-retry-publish-auditing', 'helm-array-merge-strategies', 'testem-bail-on-test-failure', 'katex-multicolumn-array-spans', 'bandit-structured-nosec-directives', 'dateutil-rfc5545-timezone-interop', 'fd-deterministic-multi-key-sorting', 'wasmi-trap-coredumps', 'awilix-async-container-initialization', 'happy-dom-abort-pending-body-reads']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def hash_json(value):
    return hashlib.sha256((json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)+'\n').encode()).hexdigest()


def write(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False)+'\n')


def snapshot(root):
    root = Path(root); digest = hashlib.sha256(); files = {}
    for p in sorted(root.rglob('*')):
        if p.is_symlink():
            raise ValueError(f'symlink forbidden: {p}')
        if p.is_file():
            name = p.relative_to(root).as_posix(); raw = p.read_bytes()
            digest.update(name.encode()+b'\0'+raw+b'\0'); files[name] = hashlib.sha256(raw).hexdigest()
    return {'sha256': digest.hexdigest(), 'files': files}


def select(rows):
    chosen = []; used = set()
    for lang in sorted({r['language'] for r in rows}):
        group = sorted((r for r in rows if r['language'] == lang), key=lambda r: hashlib.sha256((SEED+'|'+r['id']).encode()).hexdigest())
        for r in group:
            repo = r['repository'].removesuffix('.git').lower()
            if repo not in used:
                chosen.append(r['id']); used.add(repo)
                if sum(x in chosen for x in [v['id'] for v in group]) == 2:
                    break
    if chosen != PILOT:
        raise ValueError('selection differs from approved pilot')
    return chosen


def preflight(metrics):
    errors = []
    if metrics.get('system') != 'Linux' or metrics.get('architecture') not in ('x86_64', 'amd64'):
        errors.append('LINUX_AMD64_REQUIRED')
    if metrics.get('cpus', 0) < 2:
        errors.append('CPU_CAPACITY_INSUFFICIENT')
    # Agent is stopped before verifier creation in pinned Pier. Reserve 1 GiB for host.
    if metrics.get('available_memory_bytes', 0) < 9 * 2**30:
        errors.append('MEMORY_CAPACITY_INSUFFICIENT')
    if metrics.get('free_disk_bytes', 0) < 25 * 2**30:
        errors.append('DISK_CAPACITY_INSUFFICIENT')
    return errors


def validate_binding(bundle, frozen, artifacts_root):
    if bundle.get('schema_version') != 'deepswe.native-run/1' or bundle.get('upstream_commit') != UPSTREAM or bundle.get('pier_version') != PIER:
        raise ValueError('native source/runtime identity mismatch')
    if bundle.get('task_id') != frozen['id'] or bundle.get('task_hash') != frozen['task_hash']:
        raise ValueError('native task binding mismatch')
    if bundle.get('frozen_manifest_hash') != frozen['frozen_manifest_hash']:
        raise ValueError('native cohort binding mismatch')
    if bundle.get('image_digest') is not None and '@sha256:' not in bundle['image_digest']:
        raise ValueError('image digest invalid')
    root = Path(artifacts_root).resolve()
    for name, expected in bundle.get('artifact_hashes', {}).items():
        p = (root/name).resolve()
        if not p.is_relative_to(root) or not p.is_file() or sha(p) != expected:
            raise ValueError(f'artifact missing/stale/unsafe: {name}')
    if bundle.get('status') != 'INFRASTRUCTURE_FAILURE' and not bundle.get('image_digest'):
        raise ValueError('executed bundle lacks image identity')


def classify(reward, ctrf, config, case, exception=None):
    if exception:
        return {'status': 'INFRASTRUCTURE_FAILURE', 'code': 'PIER_EXCEPTION', 'details': exception}
    if not isinstance(reward, dict) or not isinstance(ctrf, dict):
        return {'status': 'INFRASTRUCTURE_FAILURE', 'code': 'VERIFIER_OUTPUT_MISSING_OR_MALFORMED'}
    if reward.get('apply_failed'):
        return {'status': 'FAIL' if case == 'oracle' else 'PASS', 'code': 'PATCH_REJECTED', 'reward': reward.get('reward'), 'test_execution': False}
    tests = ctrf.get('results', {}).get('tests')
    if not isinstance(tests, list) or not tests:
        return {'status': 'INFRASTRUCTURE_FAILURE', 'code': 'EMPTY_OR_MALFORMED_CTRF'}
    f2p, p2p = config.get('f2p_node_ids', []), config.get('p2p_node_ids', [])
    if not f2p or len(f2p) != len(set(f2p)) or len(p2p) != len(set(p2p)) or set(f2p)&set(p2p):
        return {'status': 'FAIL', 'code': 'INVALID_GRADING_ID_CONFIG'}
    def node(t):
        name = t.get('name')
        if isinstance(name, str) and name.startswith(('[f2p] ', '[p2p] ')):
            return name[6:]
        return name
    ids = [node(t) for t in tests if isinstance(t, dict)]
    if len(ids) != len(tests) or len(ids) != len(set(ids)) or set(ids) != set(f2p+p2p):
        return {'status': 'INFRASTRUCTURE_FAILURE', 'code': 'CTRF_ID_SET_MISMATCH'}
    statuses = {node(t): t.get('status') for t in tests}
    if any(s not in ('passed', 'failed', 'skipped') for s in statuses.values()):
        return {'status': 'INFRASTRUCTURE_FAILURE', 'code': 'CTRF_STATUS_INVALID'}
    fp = sum(statuses[i] == 'passed' for i in f2p); pp = sum(statuses[i] == 'passed' for i in p2p)
    expected = {'f2p_total': len(f2p), 'p2p_total': len(p2p), 'f2p_passed': fp, 'p2p_passed': pp, 'reward': int(fp == len(f2p) and pp == len(p2p)), 'f2p': fp/len(f2p), 'p2p': pp/len(p2p) if p2p else 1.0, 'partial': (fp+pp)/(len(f2p)+len(p2p))}
    for k, v in expected.items():
        x = reward.get(k)
        if isinstance(x, bool) or not isinstance(x, (float, int)) or not math.isfinite(x) or abs(x-v) > 1e-9:
            return {'status': 'FAIL', 'code': 'REWARD_CTRF_INCONSISTENT', 'field': k, 'reported': x, 'computed': v}
    want = 1 if case == 'oracle' else 0
    return {'status': 'PASS' if expected['reward'] == want else 'FAIL', 'code': 'ENDPOINT_EXPECTATION_MET' if expected['reward'] == want else 'UNEXPECTED_CREDIT_OR_ORACLE_FAILURE', 'reward': reward['reward'], 'partial': reward['partial'], 'f2p_passed': fp, 'p2p_passed': pp, 'missing_tests': [t['name'] for t in tests if 'missing from report' in str(t.get('message', ''))]}


def coverage(phases):
    statuses = list(phases.values())
    complete = len(statuses) == 3 and all(x in ('PASS', 'FAIL', 'HUMAN_REVIEW_REQUIRED', 'DEFERRED_EVIDENCE_REQUIRED') for x in statuses)
    return {'all_phases_evaluated': complete, 'clean_three_phase_result': len(statuses) == 3 and all(x == 'PASS' for x in statuses), 'has_task_defect': 'FAIL' in statuses, 'has_infrastructure_blocker': 'INFRASTRUCTURE_FAILURE' in statuses}
