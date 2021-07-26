#!/usr/bin/env python3.6

import datetime
import math 
begin_time = datetime.datetime.now()

class Solution:
    def intToRoman(self, num):
        """Given an integer, convert it to a roman numeral.
        
            >>> print('1:  ', intToRoman(1))
            I

            >>> print('3:  ', intToRoman(3))
            III

            >>> print('4:  ', intToRoman(4))
            IV

            >>> print('9:  ', intToRoman(9))
            IX

            >>> print('58:  ', intToRoman(58))
            LVIII

            >>> print('1994:  ', intToRoman(1994))
            MCMXCIV

        """

        CONVERT_TO_ROMAN = {
            0: ('I', 'V'), 1: ('X', 'L'), 2: ('C', 'D'), 3: 'M'
        }
        
        pwr = 0
        final = ''

        # create place value list
        while num:
            print(f'num at start: {num}')
            digit = math.floor(num % 10)
            if digit < 4:
                for x in range(digit):
                    final += CONVERT_TO_ROMAN[pwr][0]
            if digit == 4:
                final += CONVERT_TO_ROMAN[pwr][0]
                final += CONVERT_TO_ROMAN[pwr][1]
            if 5 < digit < 9:
                final += CONVERT_TO_ROMAN[pwr][1]
                for x in range(digit - 5):
                    final += CONVERT_TO_ROMAN[pwr][0]
            if digit == 9:
                final += CONVERT_TO_ROMAN[pwr][0]
                final += CONVERT_TO_ROMAN[pwr + 1][0]

            num = ((num - (num % 10)) * 10**pwr)  
            pwr += 1
            print(f'num at end loop: {num}')
        
        return final


        # roman = ''
        # pwr = 0

        # for key in CONVERT_TO_ROMAN:
        #     if digit == key:
        #         roman += key[digit]
            
        #     while key % 10 == 0:
        #         next_digit = key / 10
        #         pwr += 1
            
        #     if next_digit + 1 == key:

        
        # elif num == 3:
        #     return 'III'
        
        # elif num == 4:
        #     return 'IV'

        # elif num == 9:
        #     return 'IX'
        
        # elif num == 58:
        #     return 'LVIII'
        
        # elif num == 1994:
        #     return 'MCMXCIV'
        
        # else:
        #     print(f'We have hit the limits of TDD Level {self.intToRoman(1)}')

s = Solution()

print('1:  ', s.intToRoman(1))
print('3:  ', s.intToRoman(3))
print('4:  ', s.intToRoman(4))
print('9:  ', s.intToRoman(9))
print('58:  ', s.intToRoman(58))
print('1994:  ', s.intToRoman(1994))

print(datetime.datetime.now() - begin_time)
        