import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from report import accounting

class CompletionAccounting(unittest.TestCase):
    def test_nonclean_outcomes_cannot_count_as_resolved(self):
        for status in ('DEFERRED_EVIDENCE_REQUIRED', 'INFRASTRUCTURE_FAILURE', 'HUMAN_REVIEW_REQUIRED', 'NOT_RUN'):
            with self.subTest(status=status):
                x=accounting({'static':'PASS','execution':'PASS','semantic':status})
                self.assertFalse(x['clean_three_phase_result'])
                self.assertFalse(x['all_phases_resolved'])
                self.assertEqual(x['all_outcomes_recorded'],status!='NOT_RUN')

    def test_failure_is_resolved_but_not_clean(self):
        x=accounting({'static':'PASS','execution':'FAIL','semantic':'PASS'})
        self.assertTrue(x['all_outcomes_recorded'])
        self.assertTrue(x['all_phases_resolved'])
        self.assertFalse(x['clean_three_phase_result'])
        self.assertTrue(accounting(dict.fromkeys(('static','execution','semantic'),'PASS'))['clean_three_phase_result'])
