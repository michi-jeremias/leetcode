"""
https://leetcode.com/problems/maximum-subarray/

Problem 10 in
https://leetcode.com/study-plan/dynamic-programming/
"""

from collections import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return sum(self.reduceList(nums))

    def reduceListLeft(self, nums):
        newnums = nums
        print(newnums)
        if len(nums) > 2:
            sumfirst = nums[0] + nums[1]
            if sumfirst < 0 and nums[1] < nums[0]:
                newnums = self.reduceList(nums[2:])

            if sumfirst < nums[1] or nums[0] < 0:
                newnums = self.reduceList(nums[1:])
            else:
                newnums = self.reduceList([sumfirst] + nums[2:])
        if len(nums) == 2:
            sumfirst = nums[0] + nums[1]
            if sumfirst < nums[0] or sumfirst < nums[1]:
                return [max(nums)]
            return nums

        return newnums

    def reduceListRight(self, nums):
        newnums = nums
        print(newnums)
        if len(nums) > 2:
            sumfirst = nums[-1] + nums[-2]
            if sumfirst < 0 and nums[-2] < nums[-1]:
                newnums = self.reduceList(nums[:-2])

            if sumfirst < nums[-2] or nums[-1] < 0:
                newnums = self.reduceList(nums[:-1])
            else:
                newnums = self.reduceList(nums[:-2] + [sumfirst])
        if len(nums) == 2:
            sumfirst = nums[-1] + nums[-2]
            if sumfirst < nums[0] or sumfirst < nums[1]:
                return [max(nums)]
            return nums
        return newnums

    def reduceList(self, nums):
        nums = self.reduceListLeft(nums)
        nums = self.reduceListRight(nums)
        return nums


sol = Solution()
sol.maxSubArray([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])  # 187

sol = Solution()
sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # 6

sol = Solution()
sol.maxSubArray([-1, -2])  # -1

sol = Solution()
sol.maxSubArray([1, 2])  # 3

