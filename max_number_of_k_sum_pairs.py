"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/

sol = Solution()
sol.maxOperations(nums=[1, 2, 3, 4], k=5)

sol = Solution()
sol.maxOperations(nums=[3, 1, 3, 4, 3], k=6)


sol = Solution()
sol.maxOperations(nums=[2, 2, 2, 3, 1, 1, 4, 1], k=4)

sol = Solution()
sol.maxOperations(nums=[48,87,82,57,69,63,33,58,71,7,44,52,81,34,68,24,20,10,3,82,59,20,59,10,66,62,51,57,3,24,10,84,3,16,77,27,90,5,35,56,27,82,21,14,20,31,23,23,15,87,73,13,8,29,27,74,80,61,77,19,10,20,4,81,74,11,63,72,77,78,32,90,77,32,85,78,48,38,63,82,69,59,85,82,43,54,44,32,71,5,69,5,42,65,61,34,13,89,76,71,77,37,6,50,53,13,30,5,86,5,88,53,23,53,38,29,83,70,36,74,68,37,15,78,17,85], k=12)
"""

from collections import defaultdict


class Solution(object):
    def maxOperations(self, nums, k):
        hash = defaultdict(int)
        num_operations = 0

        for num in nums:
            target = k - num

            if hash[target] > 0:
                hash[target] -= 1
                num_operations += 1
            else:
                hash[num] += 1

        return num_operations
