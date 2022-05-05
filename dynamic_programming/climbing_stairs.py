"""
https://leetcode.com/problems/climbing-stairs

Problem 3 in
https://leetcode.com/study-plan/dynamic-programming/
"""


from collections import defaultdict


class Solution:
    # bottom up - iteration
    def __init__(self) -> None:
        self.num_stairs = defaultdict(int)
        # number of stairs: possible ways to climb it
        self.num_stairs[1] = 1
        self.num_stairs[2] = 2

    def climbStairs(self, n: int) -> int:

        if n not in self.num_stairs:
            for elem in range(max(self.num_stairs.keys()) + 1, n + 1, 1):
                self.num_stairs[elem] = (
                    self.num_stairs[elem - 1] + self.num_stairs[elem - 2]
                )

        return self.num_stairs[n]


class Solution:
    # top down - recursion
    def __init__(self) -> None:
        self.num_stairs = defaultdict(int)
        # number of stairs: possible ways to climb it
        self.num_stairs[1] = 1
        self.num_stairs[2] = 2

    def climbStairs(self, n: int) -> int:

        if n not in self.num_stairs:
            self.climbStairs(n - 1)
            self.num_stairs[n] = self.num_stairs[n - 1] + self.num_stairs[n - 2]

        return self.num_stairs[n]


#

sol = Solution()
sol.climbStairs(10)
