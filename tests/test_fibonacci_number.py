import unittest
from dynamic_programming.fibonacci_number import Solution


class TestSolution(unittest.TestCase):
    def test_numbers(self):
        sol = Solution()
        self.assertEqual(sol.fib(5), 5)

        sol = Solution()
        self.assertEqual(sol.fib(2), 1)
