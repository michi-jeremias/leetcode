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
            if nums[i] * lastdigit >= 0:
                lastdigit += nums[i]
                startindex += 1
            else:
                break

        print(lastdigit)
        newnums = nums[startindex:-1] + [lastdigit]
        print(newnums)
        n2 = len(newnums)

        maxmax = 0
        curmax = 0

        for i in range(0, n2, 1):
            curmax += newnums[i]

            curmax = max(0, curmax)
            maxmax = max(maxmax, curmax)

        if maxmax == 0:
            return max(max(nums), max(newnums))

        return max(max(nums), max(newnums), maxmax)


sol = Solution()
sol.maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4])  # 15

sol = Solution()
sol.maxSubarraySumCircular([1, -2, 3, -2])

sol = Solution()
sol.maxSubarraySumCircular([5, -3, 5])

sol = Solution()
sol.maxSubarraySumCircular([-3, -2, -3])  # -2

sol = Solution()
sol.maxSubarraySumCircular([2, -2, 2, 7, 8, 0])  # 19


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

