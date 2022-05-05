"""
https://leetcode.com/problems/house-robber/

Problem 5 in
https://leetcode.com/study-plan/dynamic-programming/
"""

from collections import defaultdict
from typing import List


class Solution:
    # bottom up
    def __init__(self) -> None:
        # holds the max amount possibly robbed at a certain house
        self.hash = defaultdict(int)

    def rob(self, nums: List[int]) -> int:

        num_houses = len(nums)
        if num_houses == 0:
            return 0

        if num_houses == 1:
            return nums[0]

        else:
            self.hash[0] = nums[0]
            self.hash[1] = max(nums[0], nums[1])

        for n in range(2, num_houses, 1):
            self.hash[n] = max(nums[n] + self.hash[n - 2], self.hash[n - 1])

        return self.hash[num_houses - 1]

