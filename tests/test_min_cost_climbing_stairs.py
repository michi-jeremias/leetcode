import unittest
from dynamic_programming.min_cost_climbing_stairs import Solution


class TestSolution(unittest.TestCase):
    def test_minCostClimbingStairs(self):
        sol = Solution()
        self.assertEqual(sol.minCostClimbingStairs([10, 15, 20]), 15)

        sol = Solution()
        self.assertEqual(
            sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6
        )

