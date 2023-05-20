import unittest
from main import format_duration

class TestMain(unittest.TestCase):
    def test_human_redable_format(self):
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")
