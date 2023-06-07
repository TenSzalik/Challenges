import unittest
from main import next_bigger


class TestMain(unittest.TestCase):
    def test_next_bigger(self):
        self.assertEqual(next_bigger(12), 21)
        self.assertEqual(next_bigger(21), -1)
        self.assertEqual(next_bigger(513), 531)
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger(414), 441)
        self.assertEqual(next_bigger(144), 414)
