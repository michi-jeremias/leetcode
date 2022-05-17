"""
https://leetcode.com/problems/maximum-sum-circular-subarray/

Problem 11 in
https://leetcode.com/study-plan/dynamic-programming/
"""


from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        startindex = 0
        lastdigit = nums[-1]
        for i in range(0, n - 1, 1):
            if nums[i] * nums[-1] > 0:
                lastdigit += nums[i]
                startindex += 1
            else:
                break

        newnums = nums[startindex:-1] + [lastdigit]
        n2 = len(newnums)

        maxmax = 0
        curmax = 0

        for i in range(0, n2, 1):
            curmax += newnums[i]

            curmax = max(0, curmax)
            maxmax = max(maxmax, curmax)

        if maxmax == 0:
            return max(newnums)

        return max(max(newnums), maxmax)


sol = Solution()
sol.maxSubarraySumCircular([1, -2, 3, -2])

sol = Solution()
sol.maxSubarraySumCircular([5, -3, 5])

sol = Solution()
sol.maxSubarraySumCircular([-3, -2, -3])  # -2


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]

#         maxmax = 0
#         curmax = 0

#         for i in range(0, n, 1):
#             curmax += nums[i]

#             curmax = max(0, curmax)
#             maxmax = max(maxmax, curmax)

#         if maxmax == 0:
#             return max(nums)

#         return maxmax

