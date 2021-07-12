#!/usr/bin/env python3.6

import datetime
begin_time = datetime.datetime.now()

def roman_to_int(s):
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

    NUM_INT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(s) == 1:
        return NUM_INT(s)

    sum = 0
    compound_num = None
        
         # III, IV, IX, LVIII, MCMXCIV
    for index, char in enumerate(s):
        if index == 0:
            continue
        value = NUM_INT[char]
        prev_value = NUM_INT[s[index - 1]]

        if value > prev_value:
            compound_num = value - prev_value
        
        else:
            if compound_num is not None:
                sum += compound_num
                compound_num = None

            else: 
                sum += prev_value

    if compound_num is not None:
        sum += compound_num
    else: sum += NUM_INT[s[-1]]

    return sum

        

print(roman_to_int('III'))
print(roman_to_int('IV'))
print(roman_to_int('IX'))
print(roman_to_int('LVIII'))
print(roman_to_int('MCMXCIV'))

print(datetime.datetime.now() - begin_time)
