"""
https://leetcode.com/problems/delete-and-earn/

Problem 7 in
https://leetcode.com/study-plan/dynamic-programming/
"""

from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.maxpoints = defaultdict(int)

    def deleteAndEarn(self, nums: List[int]) -> int:
        num_nums = len(nums)
        if num_nums == 0:
            return 0
        if num_nums == 1:
            return nums[0]

        if num_nums == 2:
            return max(self.gain.values())

        for item in range(2, max(nums) + 1, 1):
            if item in nums:
                self.gain[item] = max(
                    self.getgain(nums[item]) + self.gain[item - 2], self.gain[item - 1]
                )

        return max(self.maxpoints.values())


sol = Solution()
sol.deleteAndEarn(nums=[3, 4, 2])

sol = Solution()
sol.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4])

