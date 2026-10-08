import unittest

from labels import file_count_label


class FileCountLabel(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(file_count_label(0), "0 files")

    def test_one(self):
        self.assertEqual(file_count_label(1), "1 file")

    def test_multiple(self):
        self.assertEqual(file_count_label(2), "2 files")


if __name__ == "__main__":
    unittest.main()
