import unittest
from dynamic_programming.house_robber_2 import Solution


class TestSolution(unittest.TestCase):
    def test_rob(self):
        sol = Solution()
        self.assertEqual(sol.rob(nums=[1, 2, 3]), 3)

        sol = Solution()
        self.assertEqual(sol.rob(nums=[1, 2, 3, 1]), 4)

        sol = Solution()
        self.assertEqual(sol.rob(nums=[1, 2, 3]), 3)  # 3

        sol = Solution()
        self.assertEqual(sol.rob(nums=[0, 0]), 0)  # 0
