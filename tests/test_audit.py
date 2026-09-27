import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_core import classify, preflight, coverage, validate_binding, UPSTREAM, PIER, sha
from probes import solve_script

class AuditTests(unittest.TestCase):
    def setUp(self):
        self.cfg={'f2p_node_ids':['new'], 'p2p_node_ids':['old']}
        self.ctrf={'results':{'tests':[{'name':'[f2p] new','status':'passed'},{'name':'[p2p] old','status':'passed'}]}}
        self.reward={'reward':1,'f2p_total':1,'p2p_total':1,'f2p_passed':1,'p2p_passed':1,'f2p':1,'p2p':1,'partial':1}
    def test_oracle(self):self.assertEqual(classify(self.reward,self.ctrf,self.cfg,'oracle')['status'],'PASS')
    def test_nop_partial(self):
        self.ctrf['results']['tests'][0]['status']='failed';self.reward.update(reward=0,f2p=0,f2p_passed=0,partial=.5)
        self.assertEqual(classify(self.reward,self.ctrf,self.cfg,'nop')['status'],'PASS')
    def test_forged_credit_is_failure(self):self.assertEqual(classify(self.reward,self.ctrf,self.cfg,'forge-reports')['status'],'FAIL')
    def test_oracle_failure(self):self.assertEqual(classify({'apply_failed':1,'reward':0},{},self.cfg,'oracle')['status'],'FAIL')
    def test_rewarded_invalid_patch(self):
        self.assertEqual(classify({'apply_failed':1,'reward':1},{},self.cfg,'nop')['status'],'FAIL')
    def test_invalid_candidate_patch(self):self.assertEqual(classify({'apply_failed':1,'reward':0},{},self.cfg,'nop')['code'],'PATCH_REJECTED')
    def test_missing_malformed_reports(self):
        for c in [None,{}, {'results':{'tests':[]}}, {'results':{'tests':'fake'}}]:
            with self.subTest(c=c):self.assertEqual(classify(self.reward,c,self.cfg,'oracle')['status'],'INFRASTRUCTURE_FAILURE')
    def test_missing_duplicate_conflicting_ids(self):
        rows=self.ctrf['results']['tests']
        for changed in [rows[:1],rows+[rows[0]],rows+[{'name':'[f2p] new','status':'failed'}]]:
            with self.subTest(changed=changed):self.assertEqual(classify(self.reward,{'results':{'tests':changed}},self.cfg,'oracle')['code'],'CTRF_ID_SET_MISMATCH')
    def test_skipped_not_passed(self):
        self.ctrf['results']['tests'][0]['status']='skipped'
        self.assertEqual(classify(self.reward,self.ctrf,self.cfg,'oracle')['code'],'REWARD_CTRF_INCONSISTENT')
    def test_empty_f2p(self):self.assertEqual(classify(self.reward,self.ctrf,{'f2p_node_ids':[],'p2p_node_ids':['old']},'oracle')['status'],'FAIL')
    def test_crash_not_model_failure(self):self.assertEqual(classify(self.reward,self.ctrf,self.cfg,'oracle',{'exception_type':'BuildError'})['status'],'INFRASTRUCTURE_FAILURE')
    def test_forged_reward(self):
        self.reward['partial']=.3
        self.assertEqual(classify(self.reward,self.ctrf,self.cfg,'oracle')['code'],'REWARD_CTRF_INCONSISTENT')
    def test_nonfinite_and_bool(self):
        for x in [float('nan'),float('inf'),True]:
            self.reward['reward']=x
            self.assertEqual(classify(self.reward,self.ctrf,self.cfg,'oracle')['status'],'FAIL')
    def test_resource_preflight(self):
        m={'system':'Linux','architecture':'x86_64','cpus':4,'available_memory_bytes':12*2**30,'free_disk_bytes':40*2**30}
        self.assertEqual(preflight(m),[])
        for key,value in [('system','Darwin'),('cpus',1),('available_memory_bytes',7*2**30),('free_disk_bytes',14*2**30),('architecture','arm64')]:
            self.assertTrue(preflight({**m,key:value}))
    def test_phase_coverage(self):
        self.assertFalse(coverage({'static':'PASS','execution':'NOT_RUN','semantic':'PASS'})['clean_three_phase_result'])
        self.assertFalse(coverage({'static':'PASS','execution':'PASS','semantic':'HUMAN_REVIEW_REQUIRED'})['clean_three_phase_result'])
        self.assertTrue(coverage({'static':'PASS','execution':'PASS','semantic':'PASS'})['clean_three_phase_result'])
    def test_binding_and_artifacts(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'log';p.write_text('result')
            frozen={'id':'x','task_hash':'a'*64,'frozen_manifest_hash':'b'*64}
            bundle={'schema_version':'deepswe.native-run/1','upstream_commit':UPSTREAM,'pier_version':PIER,'task_id':'x','task_hash':'a'*64,'frozen_manifest_hash':'b'*64,'status':'INFRASTRUCTURE_FAILURE','image_digest':None,'artifact_hashes':{'log':sha(p)}}
            validate_binding(bundle,frozen,Path(d))
            for k,v in [('task_hash','x'),('upstream_commit','x'),('pier_version','x'),('image_digest','tag'),('frozen_manifest_hash','x')]:
                with self.assertRaises(ValueError):validate_binding({**bundle,k:v},frozen,Path(d))
            p.unlink()
            with self.assertRaises(ValueError):validate_binding(bundle,frozen,Path(d))
    def test_probe_script_syntax(self):
        cfg={**self.cfg,'grade':{'reports':['/logs/verifier/report.json']}}
        for lang in ['go','python','rust','javascript','typescript']:
            for kind in ['suppress-tests','forge-reports','protected-paths']:
                s=solve_script(kind,lang,cfg);code=s.split("'DEEPSWE_SETUP'\n",1)[1].split('\nDEEPSWE_SETUP',1)[0]
                compile(code,'setup','exec')
                import ast
                module=ast.parse(code)
                payload=next(n.value.value for n in module.body if isinstance(n,ast.Assign) and n.targets[0].id=='payload')
                compile(payload,'payload','exec')
if __name__=='__main__':unittest.main()
