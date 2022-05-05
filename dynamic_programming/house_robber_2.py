"""
https://leetcode.com/problems/house-robber-ii/

Problem 5 in
https://leetcode.com/study-plan/dynamic-programming/
"""

from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.hash1 = defaultdict()
        self.hash2 = defaultdict()

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        else:
            self.hash1[0] = nums[0]
            self.hash1[1] = max(nums[0], nums[1])
            self.hash2[1] = nums[1]
            self.hash2[2] = max(nums[1], nums[2])

            for n in range(2, len(nums) - 1, 1):
                self.hash1[n] = max(self.hash1[n - 2] + nums[n], self.hash1[n - 1])
                self.hash2[n + 1] = max(
                    self.hash2[n + 1 - 2] + nums[n + 1], self.hash2[n + 1 - 1]
                )

        return max(self.hash1[len(nums) - 2], self.hash2[len(nums) - 1])

