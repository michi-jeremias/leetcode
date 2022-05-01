from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {
            sum([nums[i], nums[j]]): [i, j]
            for i in range(len(nums) - 1, -1, -1)
            for j in range(len(nums) - 1, -1, -1)
            if i < j
        }
        return sums[target]

