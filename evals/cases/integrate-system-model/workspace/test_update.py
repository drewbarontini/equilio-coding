import unittest

from after import update_task


class UpdateTests(unittest.TestCase):
    def test_update_and_notification(self):
        tasks, events, sent = {}, [], []
        result = update_task(tasks, events, "task-1", "Review", sent.append)
        self.assertEqual(result, {"ok": True})
        self.assertEqual(tasks, {"task-1": "Review"})
        self.assertEqual(sent, [{"task_id": "task-1", "title": "Review"}])


if __name__ == "__main__":
    unittest.main()
