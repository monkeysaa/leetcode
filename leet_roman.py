class Solution:
    def romanToInt(self, s, sum = 0) -> int:
        """Given a roman numeral, convert it to an integer"""
        
        CONVERT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        if s == '':
            return sum

        value_1 = CONVERT[s[0]]
        if len(s) > 1:
            value_2 = CONVERT[s[1]]
            if value_2 > value_1:
                compound_num = value_2 - value_1
                return self.romanToInt(s[2:], sum + compound_num)

        return self.romanToInt(s[1:], sum + value_1)