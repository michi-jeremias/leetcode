"""
https://leetcode.com/problems/min-cost-climbing-stairs/

Problem 4 in
https://leetcode.com/study-plan/dynamic-programming/
"""

from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.hash = defaultdict()

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        num_stairs = len(cost)

        if num_stairs == 0:
            return 0
        if num_stairs == 1:
            return cost[0]

        else:
            self.hash[0] = cost[0]
            self.hash[1] = cost[1]

        for n in range(2, num_stairs, 1):
            self.hash[n] = min(self.hash[n - 2] + cost[n], self.hash[n - 1] + cost[n])

        return min(self.hash[num_stairs - 1], self.hash[num_stairs - 2])

