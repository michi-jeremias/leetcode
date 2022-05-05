"""
https://leetcode.com/problems/fibonacci-number/

Problem 1 in
https://leetcode.com/study-plan/dynamic-programming/
"""


class Solution:
    # bottom up - tabularization

    def __init__(self) -> None:
        self.hash = dict()
        self.hash[0] = 0
        self.hash[1] = 1

    def fib(self, n: int) -> int:

        if n not in self.hash:
            for item in range(max(self.hash.keys()) + 1, n + 1, 1):
                self.hash[item] = self.hash[item - 1] + self.hash[item - 2]

        return self.hash[n]


class Solution:
    # top down - memoization/recursion

    def __init__(self) -> None:
        self.hash = dict()
        self.hash[0] = 0
        self.hash[1] = 1

    def fib(self, n: int) -> int:

        if n not in self.hash:
            self.fib(n-1)
            self.hash[n] = self.hash[n - 1] + self.hash[n - 2]

        return self.hash[n]

sol = Solution()
sol.fib(50)
