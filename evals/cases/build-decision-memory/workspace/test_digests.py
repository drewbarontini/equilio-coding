import unittest

from digests import queue_digest, send_digest


class DigestTests(unittest.TestCase):
    def test_queue_includes_enabled_people(self):
        self.assertEqual(queue_digest({"alex": True, "sam": False}), ["alex"])

    def test_send_reaches_queued_people(self):
        sent = []
        send_digest(["alex"], {"alex": True}, sent.append)
        self.assertEqual(sent, ["alex"])


if __name__ == "__main__":
    unittest.main()
