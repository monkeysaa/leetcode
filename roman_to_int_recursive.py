#!/usr/bin/env python3.6

import datetime
begin_time = datetime.datetime.now()

def convert_roman_recursively(roman, sum=0):
    """Convert roman numeral string to an integer.
    >>> print('I:  ', roman_to_int('I'))
    1
    >>> print(roman_to_int('III'))
    3
    >>> print(roman_to_int('IV'))
    4
    >>> print(roman_to_int('IX'))
    9
    >>> print(roman_to_int('LVIII'))
    58
    >>> print(roman_to_int('MCMXCIV'))
    1994

    """
    # import pdb; pdb.set_trace()
    CONVERT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if roman == '':
        return sum
    
    value_1 = CONVERT[roman[0]]
    if len(roman) > 1:
        value_2 = CONVERT[roman[1]]
        if value_2 > value_1:
            compound_num = value_2 - value_1
            return convert_roman_recursively(roman[2:], sum + compound_num)

    return convert_roman_recursively(roman[1:], sum + value_1)

    

print(convert_roman_recursively('I'))
print(convert_roman_recursively('III'))
print(convert_roman_recursively('IV'))
print(convert_roman_recursively('IX'))
print(convert_roman_recursively('LVIII'))
print(convert_roman_recursively('MCMXCIV'))

print(datetime.datetime.now() - begin_time)