"""
https://leetcode.com/problems/n-th-tribonacci-number

Problem 2 in
https://leetcode.com/study-plan/dynamic-programming/
"""


class Solution:
    # bottom up iterative solution
    def __init__(self) -> None:
        self.hash = dict()
        self.hash[0] = 0
        self.hash[1] = 1
        self.hash[2] = 1

    def tribonacci(self, n: int) -> int:

        if n not in self.hash:
            for elem in range(3, n + 1):
                self.hash[elem] = (
                    self.hash[elem - 1] + self.hash[elem - 2] + self.hash[elem - 3]
                )

        return self.hash[n]


class Solution:
    # top down recursive solution
    def __init__(self) -> None:
        self.hash = dict()
        self.hash[0] = 0
        self.hash[1] = 1
        self.hash[2] = 1

    def tribonacci(self, n: int) -> int:

        if n not in self.hash:
            self.tribonacci(n - 1)
            self.hash[n] = self.hash[n - 1] + self.hash[n - 2] + self.hash[n - 3]

        return self.hash[n]


sol = Solution()
sol.tribonacci(4)
