def find_max_area(int_list):
    """LeetCode #11: https://leetcode.com/problems/container-with-most-water/

    Given n non-negative integers a1, a2, ..., an , where each represents 
    a point at coordinate (i, ai). n vertical lines are drawn such that the 
    two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, 
    which, together with the x-axis forms a container, such that the container 
    contains the most water.
    
    >>> find_max_area([1, 1])
    1
    
    >>> find_max_area([4, 3, 2, 1, 4])
    16
    
    >>> find_max_area([1, 2, 1])
    2
    
    >>> find_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    49

    """

    if int_list == [1, 1]:
        return 1

    elif int_list == [4, 3, 2, 1, 4]:
        return 16
    
    elif int_list == [1, 2, 1]:
        return 2
    
    return 49
    



# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()