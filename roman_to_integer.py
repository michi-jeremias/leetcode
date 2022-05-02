"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        self.found = []
        self.roman_add = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        self.roman_subtract = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": "400",
            "CM": "900",
        }

        roman_after_sub = self.process_subtract(s)
        roman_after_add = self.process_add(roman_after_sub)
        return sum(self.found)

    def process_subtract(self, roman: str):
        new_roman = ""
        for key in self.roman_subtract.keys():
            idx = roman.find(key)
            if idx != -1:
                self.found.append(self.roman_subtract[key])
                new_roman = roman[:idx] + roman[idx + 2 :]
                self.process_subtract(new_roman)

        return new_roman

    def process_add(self, roman: str):
        new_roman = ""
        for key in self.roman_add.keys():
            idx = roman.find(key)
            if idx != -1:
                self.found.append(self.roman_add[key])
                new_roman = roman[:idx] + roman[idx + 1 :]
                self.process_add(new_roman)

        return new_roman


sol = Solution()
sol.romanToInt("XIX")

