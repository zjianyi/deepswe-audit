"""Explicit authorization boundary for the 103-task expansion."""
from audit_core import hash_json


def validate_expansion(manifest, frozen):
    expected = [r['id'] for r in frozen['tasks'] if r['id'] not in frozen['pilot']]
    if (manifest.get('schema_version') != 'deepswe.expansion-cohort/1'
        or manifest.get('upstream_commit') != frozen['upstream_commit']
        or manifest.get('frozen_manifest_hash') != frozen['manifest_hash']
        or manifest.get('excluded_pilot') != frozen['pilot']
        or manifest.get('tasks') != expected or len(expected) != 103
        or manifest.get('manifest_hash') != hash_json({k:v for k,v in manifest.items() if k!='manifest_hash'})):
        raise ValueError('EXPANSION_COHORT_BINDING_MISMATCH')
    return expected


def accepted_attack_reward(case, reward, verifier_result, exception):
    return (case not in ('oracle', 'nop') and not exception
            and isinstance(reward,dict) and reward.get('reward') == 1
            and isinstance(verifier_result,dict) and verifier_result.get('rewards',{}).get('reward') == 1)
