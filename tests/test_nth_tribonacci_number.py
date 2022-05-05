import unittest

from dynamic_programming.nth_tribonacci_number import Solution


class TestSolution(unittest.TestCase):
    def test_tribonacci(self):
        sol = Solution()
        self.assertEqual(sol.tribonacci(25), 1389537)
