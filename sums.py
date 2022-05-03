from typing import List


# class Solution:
#     # Brute force
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         sums = {
#             sum([nums[i], nums[j]]): [i, j]
#             for i in range(len(nums) - 1, -1, -1)
#             for j in range(len(nums) - 1, -1, -1)
#             if i < j
#         }
#         return sums[target]


class Solution:
    # One pass hash table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in sums.keys():
                return [sums[complement], index]
            else:
                sums[num] = index

