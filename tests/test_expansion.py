import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from cohort import validate_expansion, accepted_attack_reward
from audit_core import hash_json

class ExpansionTests(unittest.TestCase):
    def test_exact_complement(self):
        f=json.loads((ROOT/'manifests/frozen.json').read_text());c=json.loads((ROOT/'manifests/expansion.json').read_text())
        ids=validate_expansion(c,f)
        self.assertEqual(len(ids),103)
        self.assertFalse(set(ids)&set(f['pilot']))
        self.assertEqual(set(ids)|set(f['pilot']),{r['id'] for r in f['tasks']})

    def test_rehashed_substitution_is_rejected(self):
        f=json.loads((ROOT/'manifests/frozen.json').read_text());c=json.loads((ROOT/'manifests/expansion.json').read_text())
        for change in ('pilot','duplicate','stale'):
            altered=copy.deepcopy(c)
            if change=='pilot':altered['tasks'][0]=f['pilot'][0]
            elif change=='duplicate':altered['tasks'][0]=altered['tasks'][1]
            else:altered['frozen_manifest_hash']='stale'
            altered['manifest_hash']=hash_json({k:v for k,v in altered.items() if k!='manifest_hash'})
            with self.assertRaises(ValueError):validate_expansion(altered,f)

    def test_native_reward_acceptance_requires_pier_corroboration(self):
        reward={'reward':1};verifier={'rewards':{'reward':1}}
        self.assertTrue(accepted_attack_reward('protected-paths',reward,verifier,None))
        self.assertFalse(accepted_attack_reward('oracle',reward,verifier,None))
        self.assertFalse(accepted_attack_reward('protected-paths',reward,{},None))
        self.assertFalse(accepted_attack_reward('protected-paths',reward,verifier,{'error':'crash'}))
        self.assertFalse(accepted_attack_reward('forge-reports',{'reward':0},verifier,None))
