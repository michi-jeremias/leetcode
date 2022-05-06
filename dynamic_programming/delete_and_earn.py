"""
https://leetcode.com/problems/delete-and-earn/

Problem 7 in
https://leetcode.com/study-plan/dynamic-programming/
"""

from collections import defaultdict
from email.policy import default
from typing import List


class Solution:
    def __init__(self) -> None:
        self.gain = defaultdict(int)
        self.hash = defaultdict(int)

    def deleteAndEarn(self, nums: List[int]) -> int:
        maxnum = max(nums)
        if maxnum == 0:
            return 0
        if maxnum == 1:
            return nums.count(1)

        for n in range(0, maxnum + 1, 1):
            self.gain[n] = nums.count(n) * n

        self.hash[1] = self.gain[1]

        def get_cumulated_gain(num):
            for n in range(num, 0, -1):
                if n not in self.hash:
                    get_cumulated_gain(n - 1)
                    self.hash[n] = max(
                        self.gain[n] + self.hash[n - 2], self.hash[n - 1]
                    )
                return self.hash[n]

        # get_cumulated_gain(maxnum)

        # return self.hash[maxnum]
        return get_cumulated_gain(maxnum)


sol = Solution()
sol.deleteAndEarn(nums=[3, 4, 2])

sol = Solution()
sol.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4])

sol = Solution()
sol.deleteAndEarn(nums=[1])

sol = Solution()
sol.deleteAndEarn(nums=[1, 1, 1, 2, 4, 5, 5, 5, 6])

