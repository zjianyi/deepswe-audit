"""Recovery must preserve the one-shot S0 evidence and never invoke a reviewer."""
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import local_audit


class SemanticRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.task='expansion-fixture'
        self.out=self.root/'.local/phase3'/self.task
        self.out.mkdir(parents=True)
        self.public=self.root/'evidence/expansion'/self.task/'semantic.json'
        self.reviewer=types.ModuleType('btqc.semantic.reviewer')
        self.reviewer.prepare_semantic_input=Mock(side_effect=AssertionError('must not regenerate input'))
        self.reviewer.review_semantic_input=Mock(side_effect=AssertionError('must not launch S0'))
        for context in (
            patch.object(local_audit,'ROOT',self.root),
            patch.object(local_audit,'frozen',return_value={'pilot':[]}),
            patch.dict(sys.modules,{'btqc.semantic.reviewer':self.reviewer}),
        ):
            context.start()
            self.addCleanup(context.stop)

    def test_started_attempt_refuses_before_mutating_input(self):
        original=b'{"frozen": "first attempt"}\n'
        marker=b'{"sequence": "S0", "input_sha256": "retained"}\n'
        (self.out/'input.json').write_bytes(original)
        (self.out/'attempt.json').write_bytes(marker)
        with self.assertRaisesRegex(RuntimeError,'S0 attempt already started'):
            local_audit.semantic(self.task)
        self.assertEqual((self.out/'input.json').read_bytes(),original)
        self.assertEqual((self.out/'attempt.json').read_bytes(),marker)
        self.assertFalse(self.public.exists())
        self.reviewer.prepare_semantic_input.assert_not_called()
        self.reviewer.review_semantic_input.assert_not_called()

    def test_local_outcome_backfills_public_copy_without_reviewer(self):
        # Both a completed finding and a recorded validation blocker are terminal attempts.
        for status in ('FAIL','INFRASTRUCTURE_FAILURE'):
            with self.subTest(status=status):
                result=(json.dumps({'overall_status':status},indent=3)+'\n').encode()
                (self.out/'semantic.json').write_bytes(result)
                (self.out/'attempt.json').write_text('{"sequence":"S0"}')
                local_audit.semantic(self.task)
                self.assertEqual(self.public.read_bytes(),result)
                self.assertEqual((self.out/'semantic.json').read_bytes(),result)
                self.public.unlink()
        self.reviewer.prepare_semantic_input.assert_not_called()
        self.reviewer.review_semantic_input.assert_not_called()

    def test_existing_public_outcome_is_never_overwritten(self):
        (self.out/'semantic.json').write_text('{"overall_status":"FAIL"}')
        self.public.parent.mkdir(parents=True)
        original=b'{"overall_status": "FAIL", "retained": true}\n'
        self.public.write_bytes(original)
        local_audit.semantic(self.task)
        self.assertEqual(self.public.read_bytes(),original)

    def test_partial_local_outcome_is_not_published(self):
        (self.out/'semantic.json').write_text('{"overall_status":')
        with self.assertRaises(json.JSONDecodeError):local_audit.semantic(self.task)
        self.assertFalse(self.public.exists())
        self.reviewer.prepare_semantic_input.assert_not_called()
        self.reviewer.review_semantic_input.assert_not_called()
