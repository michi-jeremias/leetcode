import unittest

from dynamic_programming.climbing_stairs import Solution


class TestSolution(unittest.TestCase):
    def test_climb_stairs(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(2), 2)
        self.assertEqual(sol.climbStairs(3), 3)
        self.assertEqual(sol.climbStairs(10), 89)
