import unittest
from max_number_of_k_sum_pairs import Solution


class TestSolution(unittest.TestCase):
    def test_numbers(self):
        sol = Solution()
        self.assertEqual(sol.maxOperations([1, 2, 3, 4], 5), 2)
        sol = Solution()
        self.assertEqual(sol.maxOperations([3, 1, 3, 4, 3], 6), 1)
        sol = Solution()
        self.assertEqual(sol.maxOperations([3, 3, 3], 6), 1)

    def test_empty_array(self):
        sol = Solution()
        self.assertEqual(sol.maxOperations([], 5), 0)

    def test_signed_integers(self):
        sol = Solution()
        self.assertEqual(sol.maxOperations([-1, 1, 2, 6], 5), 1)

