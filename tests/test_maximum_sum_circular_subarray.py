import unittest
from dynamic_programming.maximum_sum_circular_subarray import Solution


class TestSolution(unittest.TestCase):
    def test_maxSubarraySumCircular(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([1, -2, 3, -2]), 3)
        sol = Solution()
        self.assertEqual(sol.maxSubArray([5, -3, 5]), 10)
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-3, -2, -3]), -2)

