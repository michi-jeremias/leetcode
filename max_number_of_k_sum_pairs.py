"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/

sol = Solution()
sol.maxOperations(nums=[1, 2, 3, 4], k=5)

sol = Solution()
sol.maxOperations(nums=[3, 1, 3, 4, 3], k=6)
"""


from typing import List


class Solution:
    def __init__(self) -> None:
        self.num_operations = 0

    def maxOperations(self, nums: List[int], k: int) -> int:
        values = {}

        new_nums = nums

        for index, item in enumerate(new_nums):
            complement = k - item

            if complement in values.keys():
                values.pop(complement)
                new_nums.pop(new_nums.index(complement))
                new_nums.pop(new_nums.index(item))
                self.num_operations += 1
                self.maxOperations(new_nums, k)
            else:
                values[item] = index

        return self.num_operations


sol = Solution()
sol.maxOperations(nums=[2, 2, 2, 3, 1, 1, 4, 1], k=4)

