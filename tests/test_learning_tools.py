from datetime import datetime, timezone
from pathlib import Path
import unittest

from learning_tools import (
    ProgressStore,
    check,
    code_check,
    review_queue,
    review_interval,
    short_answer_check,
)

ROOT = Path(__file__).resolve().parents[1]
TMP_ROOT = ROOT / ".test_tmp"


class LearningToolsTests(unittest.TestCase):
    def setUp(self):
        TMP_ROOT.mkdir(exist_ok=True)

    def test_review_interval_defaults(self):
        self.assertLess(review_interval(False, 3, 1).total_seconds(), review_interval(True, 5, 1).total_seconds())
        self.assertEqual(review_interval(True, 3, 1).days, 3)
        self.assertEqual(review_interval(True, 5, 3).days, 30)

    def test_progress_store_records_attempt_and_persists(self):
        path = TMP_ROOT / "progress_persist.json"
        if path.exists():
            path.unlink()
        store = ProgressStore(path)
        row = store.record_attempt("skill.one", True, confidence=5)
        self.assertEqual(row["attempts"], 1)
        self.assertEqual(row["correct"], 1)
        self.assertGreater(row["mastery"], 0.0)

        loaded = ProgressStore(path)
        self.assertIn("skill.one", loaded.data["skills"])

    def test_review_queue_returns_due_items(self):
        path = TMP_ROOT / "progress_due.json"
        if path.exists():
            path.unlink()
        store = ProgressStore(path)
        row = store.get("skill.due")
        row.update({"attempts": 1, "correct": 0, "mastery": 0.1, "next_review": "2000-01-01T00:00:00+00:00"})
        store.save()
        due = store.review_queue(now=datetime(2026, 1, 1, tzinfo=timezone.utc))
        self.assertEqual(due[0]["id"], "skill.due")
        self.assertEqual(review_queue(store=store)[0]["id"], "skill.due")

    def test_checks_return_boolean(self):
        self.assertTrue(check("simple", 2 + 2, 4))
        self.assertFalse(check("simple", 2 + 2, 5))
        self.assertTrue(short_answer_check("answer", " X = 7 ", ["x=7", "7"]))
        self.assertTrue(code_check("fn", lambda x: x + 1, [((1,), 2), ((2,), 3)]))


if __name__ == "__main__":
    unittest.main()
