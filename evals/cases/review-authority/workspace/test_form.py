import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parent / "head"))
from form import submit


class FormTests(unittest.TestCase):
    def test_blank_title(self):
        tasks = []
        self.assertEqual(submit(tasks, " ")["field"], "title")
        self.assertEqual(tasks, [])
