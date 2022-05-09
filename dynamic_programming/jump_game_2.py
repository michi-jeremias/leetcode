"""
https://leetcode.com/problems/jump-game-ii/

Problem 9 in
https://leetcode.com/study-plan/dynamic-programming/
"""


from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.hash = defaultdict(int)

    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return 1

        self.hash[0] = 1
        self.hash[1] = 1

        current_jumps = 1
        for i in range(2, n, 1):

            for j in range(0, i, 1):
                if nums[j] >= i - j:
                    pass

            pass


sol = Solution()
sol.jump([2, 3, 1, 1, 4])
nums = [2, 3, 1, 1, 4]  # 2
