# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        result = 0
        while s:
            cur_num = s[:2]
            if cur_num not in numbers:
                cur_num = s[0]
            result += numbers[cur_num]
            s = s[len(cur_num):]
        return result
