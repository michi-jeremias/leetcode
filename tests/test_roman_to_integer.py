import unittest
from roman_to_integer import Solution


class TestSolution(unittest.TestCase):
    def test_single_digit(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("X"), 10)

    def test_multiple_single_digits(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("XX"), 20)
        self.assertEqual(sol.romanToInt("II"), 2)
        self.assertEqual(sol.romanToInt("MM"), 2000)
        self.assertEqual(sol.romanToInt("MV"), 1005)

    def test_double_digit(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("IV"), 4)
        self.assertEqual(sol.romanToInt("IX"), 9)
        self.assertEqual(sol.romanToInt("XL"), 40)
        self.assertEqual(sol.romanToInt("XC"), 90)
        self.assertEqual(sol.romanToInt("CD"), 400)
        self.assertEqual(sol.romanToInt("CM"), 900)

    def test_mixed_digits(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("LVIII"), 58)
        self.assertEqual(sol.romanToInt("MCMXCIV"), 1994)

