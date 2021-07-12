#!/usr/bin/env python3.6

import datetime
begin_time = datetime.datetime.now()

class Solution:
    def longestCommonPrefix(self, my_str):

        prefix = ""
        sorted_strs = sorted(strs)
        len_first_word = len(sorted_strs[0])
        
        for i in range(len_first_word):
            if sorted_strs[0][i] == sorted_strs[-1][i]:
                prefix += sorted_strs[0][i]
            else:
                return prefix
                
        return prefix

s = Solution()
print(s.longestCommonPrefix(['flow', 'flower', 'flight']))
print(datetime.datetime.now() - begin_time)