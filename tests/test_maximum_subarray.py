import unittest
from dynamic_programming.maximum_subarray import Solution


class TestSolution(unittest.TestCase):
    def test_maxSubArray(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        sol = Solution()
        self.assertEqual(sol.maxSubArray([1]), 1)
        sol = Solution()
        self.assertEqual(sol.maxSubArray([5, 4, -1, 7, 8]), 23)
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-1, -2]), -1)
        sol = Solution()
        self.assertEqual(sol.maxSubArray([1, 2]), 3)
        sol = Solution()
        self.assertEqual(
            sol.maxSubArray([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]), 187
        )

