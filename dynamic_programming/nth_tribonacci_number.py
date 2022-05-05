class Solution:
    def __init__(self) -> None:
        hash = dict()
        hash[0] = 0
        hash[1] = 1
        hash[2] = 1

    def tribonacci(self, n: int) -> int:

        if n not in self.hash:
            for elem in range(3, n + 1):
                hash[elem] = hash[elem - 1] + hash[elem - 2] + hash[elem - 3]

        return hash[n]
