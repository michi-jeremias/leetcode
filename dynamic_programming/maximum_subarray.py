"""
https://leetcode.com/problems/maximum-subarray/

Problem 10 in
https://leetcode.com/study-plan/dynamic-programming/
"""

from collections import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass

    def find_max_interval(self, nums) -> List[int]:

        if len(nums) > 1:
            start = 0
            mid = len(nums) // 2
            end = len(nums) - 1

            self.find_max_interval(nums[start : mid + 1])
            self.find_max_interval(nums[mid : end + 1])

        else:
            return nums

