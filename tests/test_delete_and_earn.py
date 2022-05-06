import unittest
from dynamic_programming.delete_and_earn import Solution


class TestSolution(unittest.TestCase):
    def test_delete_and_earn(self):
        sol = Solution()
        self.assertEqual(sol.delete_and_earn([3, 4, 2]), 6)
        sol = Solution()
        self.assertEqual(sol.delete_and_earn([2, 2, 3, 3, 3, 4]), 9)
