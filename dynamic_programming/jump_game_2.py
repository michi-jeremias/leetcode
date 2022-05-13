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

    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        self.min_jumps_needed[0] = 0
        for i in range(1, n):
            self.min_jumps_needed[i] = 1e5

        current_min_jumps = 1
        max_index_reached = 0

        for current_position in range(0, n - 1, 1):
            current_num = nums[current_position]

            if (
                current_position + current_num > max_index_reached
                and max_index_reached < n
            ):
                for step in range(1, current_num + 1, 1):
                    if current_position + step <= n - 1:
                        self.min_jumps_needed[current_position + step] = min(
                            current_min_jumps,
                            self.min_jumps_needed[current_position] + 1,
                            self.min_jumps_needed[current_position + step],
                        )

                max_index_reached = min(
                    max(max_index_reached, current_position + current_num), n - 1
                )

                current_min_jumps = self.min_jumps_needed[max_index_reached] + 1
        return self.min_jumps_needed[n - 1]

