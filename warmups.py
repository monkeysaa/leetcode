def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    numset = set(nums)

    for num in numset:
        if num * -1 in numset and num != 0:
            return True
    
    # handle edge case where nums has two zeros
    # for index, value in enumerate(nums):
    #     if value == 0:
    #         if 0 in nums[index+1:]:
    #             return True
    
    # or, with list comprehension:
    zeros = [index for index, value in enumerate(nums) if value == 0]
    return len(zeros) > 1
 

    return False


