"""
https://leetcode.com/problems/delete-and-earn/

Problem 7 in
https://leetcode.com/study-plan/dynamic-programming/
"""

from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.gains = defaultdict(int)
        self.values = defaultdict(int)

    def deleteAndEarn(self, nums: List[int]) -> int:

        maxnum = max(nums)

        for n in range(0, maxnum, 1):
            self.gains[n] = nums.count(n) * n

        def get_value(num):
            for num in set(nums):
                if num == 0:
                    return 0
                if num == 1:
                    return self.points[1]

                if num not in self.values.keys():
                    self.get_value(num - 1)
                    self.values[num] = max(
                        self.gains[num] + self.gains[num - 2], self.gains[num - 1]
                    )

        return max(self.values.values())


class Solution:
    def __init__(self) -> None:
        self.points = defaultdict(int)

    def deleteAndEarn(self, nums: List[int]) -> int:
        maxnum = 0

        for num in nums:
            self.points[num] += num
            maxnum = max(num, maxnum)

        if num == 0:
            return 0
        if num == 1:
            return self.points[1]

        if num not in self.points:
            self.deleteAndEarn(num - 1)
            self.points[num] = max(
                self.points[num] + self.points[num - 2], self.points[num - 1]
            )

        return max(self.points.values())


sol = Solution()
sol.deleteAndEarn(nums=[3, 4, 2])

sol = Solution()
sol.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4])

