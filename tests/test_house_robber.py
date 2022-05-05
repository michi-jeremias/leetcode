import unittest

from dynamic_programming.house_robber import Solution


class TestSolution(unittest.TestCase):
    def test_robber(self):
        sol = Solution()
        self.assertEqual(sol.rob([1, 2, 3, 1]), 4)

        sol = Solution()
        self.assertEqual(sol.rob([1, 4, 1, 1, 8, 8, 1]), 13)

        sol = Solution()
        self.assertEqual(sol.rob([2, 1, 1, 2]), 4)
