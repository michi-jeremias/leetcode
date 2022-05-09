import unittest

from dynamic_programming.jump_game import Solution


class TestSolution(unittest.TestCase):
    def test_cases(self):
        sol = Solution()
        self.assertEqual(sol.canJump([2, 3, 1, 1, 4]), True)
        sol = Solution()
        self.assertEqual(sol.canJump([3, 2, 1, 0, 4]), False)
        sol = Solution()
        self.assertEqual(sol.canJump([0]), True)
        sol = Solution()
        self.assertEqual(sol.canJump([0, 2, 3]), False)
        sol = Solution()
        self.assertEqual(sol.canJump([0, 1]), False)

