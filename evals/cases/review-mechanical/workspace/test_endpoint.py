import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parent / "head"))
from handler import public_release


class ReleaseTests(unittest.TestCase):
    def test_cache_policy_preserves_public_payload(self):
        self.assertEqual(public_release("1.2"), {
            "status": 200, "body": {"version": "1.2", "channel": "stable"},
            "headers": {"Cache-Control": "public, max-age=60"}})
