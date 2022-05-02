from math import ceil, log10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.digits = {}
        length_x = self.getLength(x)
        self.get_digits(x)
        new_x = self.get_new_x(length_x)

        if x == new_x and x >= 0:
            return True
        else:
            return False

    def getLength(self, x: int) -> int:
        length = max(ceil(log10(abs(x) + 1)), 1)
        return length

    def get_digits(self, x) -> None:
        length = self.getLength(x)
        first_digit, _ = divmod(x, 10 ** (length - 1))
        new_x = x - first_digit * 10 ** (length - 1)
        self.digits[self.getLength(x) - 1] = first_digit
        if length - 1 > 0:
            self.get_digits(new_x)

    def get_new_x(self, length) -> int:
        sum = 0
        for k in self.digits.keys():
            new_power = abs(k - length + 1)
            sum += self.digits[k] * 10 ** new_power
        return sum
