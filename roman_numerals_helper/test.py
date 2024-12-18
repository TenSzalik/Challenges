import unittest
from main import RomanNumerals


class TestMain(unittest.TestCase):
    def test_to(self):
        self.assertEqual(RomanNumerals.to_roman(1000), 'M')
        self.assertEqual(RomanNumerals.to_roman(4), 'IV')
        self.assertEqual(RomanNumerals.to_roman(1), 'I')
        self.assertEqual(RomanNumerals.to_roman(1990), 'MCMXC')
        self.assertEqual(RomanNumerals.to_roman(2008), 'MMVIII')

    def test_from(self):
        self.assertEqual(RomanNumerals.from_roman('XXI'), 21)
        self.assertEqual(RomanNumerals.from_roman('I'), 1)
        self.assertEqual(RomanNumerals.from_roman('IV'), 4)
        self.assertEqual(RomanNumerals.from_roman('MMVIII'), 2008)
        self.assertEqual(RomanNumerals.from_roman('MDCLXVI'), 1666)
