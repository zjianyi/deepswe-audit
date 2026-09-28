import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from semantic_capture import run_once

class CaptureTests(unittest.TestCase):
    def test_rejected_output_is_archived_and_attempt_not_repeated(self):
        class Error(RuntimeError):
            code='REVIEW_OUTPUT_INVALID';message='invalid fixture';evidence={}
        class Backend:
            def __init__(self,*args):pass
            def review(self,bundle,schema,output):
                output.write_text('{"invalid":true}')
                return {'invalid':True}
        module=types.ModuleType('btqc.semantic.codex');module.CodexCliReviewer=Backend;module.SemanticInfrastructureError=Error
        with tempfile.TemporaryDirectory() as tmp, patch.dict(sys.modules,{'btqc.semantic.codex':module}):
            out=Path(tmp)/'out';out.mkdir();(out/'input.json').write_text('{}')
            bundle=Path(tmp)/'bundle';bundle.mkdir();(bundle/'instruction.json').write_text('{}')
            def reject(inp,ledger_path,backend):
                backend.review(bundle,bundle/'schema.json',Path(tmp)/'result.json')
                raise Error()
            result=run_once(out,reject)
            self.assertEqual(result['overall_status'],'INFRASTRUCTURE_FAILURE')
            self.assertEqual(json.loads((out/'raw-review.json').read_text()),{'invalid':True})
            self.assertTrue((out/'bundle/instruction.json').exists())
            with self.assertRaises(RuntimeError):run_once(out,reject)
