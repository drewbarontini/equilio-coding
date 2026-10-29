import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parent / "head"))
from webhook import handle


class WebhookTests(unittest.TestCase):
    def test_success(self):
        sent = []
        self.assertEqual(handle({"event_id": "e1"}, set(), sent.append, lambda e: None), 200)
        self.assertEqual(sent, [{"event_id": "e1"}])

    def test_duplicate(self):
        sent, seen = [], set()
        event = {"event_id": "e1"}
        handle(event, seen, sent.append, lambda e: None)
        handle(event, seen, sent.append, lambda e: None)
        self.assertEqual(sent, [event])

    def test_missing_identifier(self):
        sent = []
        self.assertEqual(handle({}, set(), sent.append, lambda e: None), 400)
        self.assertEqual(sent, [])
