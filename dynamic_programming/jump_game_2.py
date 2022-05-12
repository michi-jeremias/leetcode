"""
https://leetcode.com/problems/jump-game-ii/

Problem 9 in
https://leetcode.com/study-plan/dynamic-programming/
"""


from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.min_jumps_needed = defaultdict(int)
        self.hash = defaultdict(int)

    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        self.min_jumps_needed[0] = 0
        for i in range(1, n):
            self.min_jumps_needed[i] = 1e5

        current_jumps = 0
        current_min_jumps = 0

        for current_position in range(0, n, 1):
            current_jumps += 1
            for step in range(1, nums[current_position] + 1, 1):
                if current_position + step <= n - 1:
                    current_min_jumps = self.min_jumps_needed[current_position + step]
                    self.min_jumps_needed[current_position + step] = min(
                        current_jumps, self.min_jumps_needed[current_position + step]
                    )
            print(self.min_jumps_needed)
            current_jumps = min(current_jumps, current_min_jumps)
        return self.min_jumps_needed[n - 1]


sol = Solution()
sol.jump([1, 2, 1, 1, 1])  # 3

sol = Solution()
sol.jump([2, 3, 1, 1, 4])  # 2

sol = Solution()
sol.jump([9, 7, 9, 4, 8, 1, 6, 1, 5, 6, 2, 1, 7, 9, 0])  # 2

