"""
https://leetcode.com/problems/jump-game/

Problem 8 in
https://leetcode.com/study-plan/dynamic-programming/
"""
# from collections import defaultdict
from typing import List


# class Solution:
#     def __init__(self) -> None:
#         self.reachable = defaultdict(bool)

#     def canJump(self, nums: List[int]) -> bool:
#         def check(nums):
#             last_index = len(nums) - 1
#             for i in range(last_index - 1, -1, -1):

#                 distance = last_index - i
#                 self.reachable[last_index] = False
#                 if nums[i] >= distance:
#                     self.reachable[last_index] = True
#                     check(nums[:-1])
#                     break

#         check(nums)
#         print(self.reachable)
#         return all(self.reachable.values())


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n <= 1:
            return True

        last_index = n - 1

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i

        return last_index == 0

