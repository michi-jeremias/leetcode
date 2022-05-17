"""
https://leetcode.com/problems/maximum-subarray/

Problem 10 in
https://leetcode.com/study-plan/dynamic-programming/
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        maxmax = 0
        curmax = 0

        for i in range(0, n, 1):
            curmax += nums[i]

            curmax = max(0, curmax)
            maxmax = max(maxmax, curmax)

        if maxmax == 0:
            return max(nums)

        return maxmax

