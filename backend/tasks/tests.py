from django.test import TestCase
from tasks.scoring import score_task

class ScoreTest(TestCase):

    def test_importance_affects_score(self):
        t = {
            "id": 1,
            "title": "A",
            "due_date": "2025-12-01",
            "estimated_hours": 5,
            "importance": 10,
            "dependencies": []
        }
        score, _ = score_task(t, [t], "smart")
        self.assertTrue(score > 10)

    def test_effort_low_gives_high_score(self):
        t = {
            "id": 1,
            "title": "A",
            "due_date": "2025-12-01",
            "estimated_hours": 1,
            "importance": 5,
            "dependencies": []
        }
        score, _ = score_task(t, [t], "smart")
        self.assertTrue(score > 10)

    def test_past_due_increases_score(self):
        t = {
            "id": 1,
            "title": "A",
            "due_date": "2020-01-01",
            "estimated_hours": 5,
            "importance": 5,
            "dependencies": []
        }
        score, _ = score_task(t, [t], "smart")
        self.assertTrue(score > 15)
        