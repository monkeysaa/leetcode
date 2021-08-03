#!/usr/bin/env python3.6

import datetime
begin_time = datetime.datetime.now()

# def add_to_zero(nums):
#     """Given list of ints, return True if any two nums sum to 0."""

#     numset = set(nums)

#     for num in numset:
#         if num * -1 in numset and num != 0:
#             return True
    
#     # handle edge case where nums has two zeros
#     # for index, value in enumerate(nums):
#     #     if value == 0:
#     #         if 0 in nums[index+1:]:
#     #             return True
    
#     # or, with list comprehension:
#     zeros = [index for index, value in enumerate(nums) if value == 0]
#     return len(zeros) > 1
 

#     return False

# def concat_lists(list1, list2):
#     """Combine lists."""

#     return list1 + list2


# def deduped(items):
#     """Return new (ordered) list from items with duplicates removed."""

#     noted = set()
#     deduped = [] 

#     for i in items:
#         if i not in noted:
#             deduped.append(i)
#             noted.add(i)
    
#     return deduped

# def is_anagram_of_palindrome(word):
#     """Is the word an anagram of a palindrome?"""

#     counter = {}
#     prev_exception = False

#     for letter in word.lower():
#         counter[letter] = counter.get(letter, 0) + 1
    
#     for count in counter.values():
#         if count % 2 != 0:
#             if prev_exception == True:
#                 return False
#             prev_exception = True

#     return True

# def has_balanced_parens(phrase):
#     """Does a string have balanced parentheses?

#     >>> has_balanced_parens("()")
#     True

#     >>> has_balanced_parens("(Oh Noes!)(")
#     False

#     >>> has_balanced_parens("((There's a bonus open paren here.)")
#     False

#     >>> has_balanced_parens(")")
#     False

#     >>> has_balanced_parens("(")
#     False

#     >>> has_balanced_parens("(This has (too many closes.) ) )")
#     False
#     """

#     started = []

#     for char in phrase:
#         if char == '(':
#             started.append('(')
#         if char == ')':
#             if started == []:
#                 return False
#             else:
#                 started.pop()
                
#     return started == []


    

# def merge_sorted(l1, l2, new_head = None):
#     """Merge two sorted singly-linked lists."""

#     if l1 is None:
#         return l2
    
#     elif l2 is None:
#         return l1
    
#     else:
#         if l1.val >= l2.val:
#             new_list = l2
#             new_list.next = merge_sorted(l1, l2.next, new_list)


# def strStr(haystack, needle):
#     if needle == "":
#         return 0
    
#     if needle in haystack:
#         counter = 0
#         first = None

#         for i, char in enumerate(haystack):
#             if char == needle[0]: 
#                 counter = 0
#                 first = i
                
#                 for l in needle:
#                     if haystack[i + counter] == l:
#                         counter += 1
#                     else:
#                         counter = 0
#                         first = None
#                         break
#                 if first is not None:
#                 ### PITFALL TO REMEMBER! 
#                 # if first:  is DANGEROUS with integer problems.
#                 # If first == 0, this statement is FALSEY and will not return ###
#                     return first
        
#     else:
#         return -1

# ### Use .index() Longstring.index(substring)
# def strStr2(haystack, needle):
#     if needle == "":
#         return 0
    
#     try: 
#         # if needle in haystack, return the index.
#         i = haystack.index(needle)
#         return i
#     except:
#         # if needle not in haystack
#         return -1

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList():
#     def __init__(self):
#         "Initiate a singly linked list."

#         self.head = None
#         self.tail = None
    
#     def append(self, item):
#         "Add item to singly linked list."

#         if self.head:
#             self.tail.next = item
#             self.tail = item
#         else:
#             self.head = item
#             self.tail = item

#     def has_item(self, item):
#         """Is a specific item in a singly linked list?"""
    
#         curr = self.head
        
#         while curr:
#             if curr == item:
#                 return True
#             curr = curr.next
        
#         return False

# ll = LinkedList()
# ll.append(Node(1))
# ll.append(Node(5))
# a = Node(6)
# ll.append(a)
# ll.append(Node(2))
# print(ll.has_item(a))

# def searchInsert(nums, target):
#     """Return the index of target in nums, or index to insert.

#     searchInsert([1,3,5,6], 5)
#     """

#     lst = nums
#     index = 0
    
#     import pdb; pdb.set_trace()
    
#     while len(lst) > 1:
#         midpoint = len(lst)//2
#         if lst[midpoint] > target:
#             lst = lst[:midpoint]
#         else:
#             lst = lst[midpoint:]
#             index += midpoint
    
#     if lst[0] >= target:
#         return index
    
#     if lst[0] < target:
#         return index + 1    

# def maxSubArray(nums):
#     """ LeetCode 53: https://leetcode.com/problems/maximum-subarray/

#     Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#     A subarray is a contiguous part of an array.

#     >>> maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#     6

#     >>> maxSubArray([1])
#     1

#     >>> maxSubArray([5, 4, -1, 7, 8])
#     23

#     >>> maxSubArray([-5, -4, -1, -7, -8])
#     -1
#     """
#     max_sum = max(nums)
#     maybe_max = []
#     curr_sum = 0
    
#     for num in nums:
#         if maybe_max == [] and num <= 0:
#             continue
#         elif maybe_max == [] and num > 0:
#             maybe_max =[num]
#             curr_sum += num
#         else: # maybe_max isn't empty
#             if curr_sum + num > 0:
#                 maybe_max.append(num)
#                 curr_sum += num
#             else: 
#                 maybe_max = []
#                 curr_sum = 0
#         if curr_sum > max_sum:
#             max_sum = curr_sum
    
#     return max_sum

# def plusOne(digits):
#     if digits[-1] + 1 < 10:
#         digits[-1] = digits[-1] + 1
#         return digits
#     else:
#         power_of_ten = len(digits) - 1
#         sum_num = 0
#         for i, num in enumerate(digits):
#             sum_num += num * 10**power_of_ten
#             power_of_ten -= 1
#         result = sum_num + 1
#         return [int(char) for char in str(result)]

# def is_palindrome(word):
#     """Is the word an anagram of a palindrome?

#     >>> is_palindrome("a")
#     True

#     >>> is_palindrome("ab")
#     False

#     >>> is_palindrome("arceace")
#     False

#     >>> is_palindrome("racecar")
#     True
#     """

#     midpoint = len(word) // 2
#     if len(word) == 1 or word[:midpoint] == word[:midpoint:-1]:
#             return True
#     return False

# def is_anagram_of_palindrome(word):
#     """Is the word an anagram of a palindrome?
    
#     >>> is_anagram_of_palindrome("a")
#     True

#     >>> is_anagram_of_palindrome("ab")
#     False

#     >>> is_anagram_of_palindrome("aab")
#     True

#     >>> is_anagram_of_palindrome("arceace")
#     True

#     >>> is_anagram_of_palindrome("arceaceb")
#     False
#     """

#     # for letter in word, are there an even number of letters? 
#     # 1 exception allowed. 

#     letter_match = set()
#     for letter in word:
#         if letter in letter_match:
#             letter_match.remove(letter)
#         else:
#             letter_match.add(letter)
#     if len(letter_match) > 1:
#         return False
#     return True


# def has_more_vowels(word):
#     """Does word contain more vowels than non-vowels?
#     >>> has_more_vowels("moose")
#     True

#     >>> has_more_vowels("mice")
#     False

#     >>> has_more_vowels("graph")
#     False

#     >>> has_more_vowels("yay")
#     False

#     >>> has_more_vowels("Aal")
#     True
#     """
#     # define vowels
#     # find length of word
#     # count vowels (use .lower())
#     # if num vowels > half length of word, return True

#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     half = len(word)//2
#     num_vowels = 0

#     for char in word.lower():
#         if char in vowels:
#             num_vowels += 1
    
#     if num_vowels > half:
#         return True
#     return False

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.
    
    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """
    import math
    assert 0 < val < 101, "Val must be between 1-100"
    guess = 50
    half = guess//2 #25

    num_guesses = 1

    while guess != val: #50, 75
        num_guesses += 1 #1
        if guess > val:
            guess -= half #
        elif guess < val: 
            guess += half #75
        half = math.ceil(half/2) #
        
    return num_guesses
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(datetime.datetime.now() - begin_time)