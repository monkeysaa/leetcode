import datetime
begin_time = datetime.datetime.now()

def jump_game_ii(nums):
    """LeetCode #45: https://leetcode.com/problems/jump-game-ii/

    Given an array of non-negative integers nums, you are initially positioned 
    at the first index of the array.
    
    Each element in the array represents your max jump length at that position.
    Your goal is to reach the last index in the minimum number of jumps.
    You can assume that you can always reach the last index.
    
    The solution treats jumps as a tiered tree without explicitly building one.
    Each tier includes a set of indices that can be reached in that #jumps.
    These indices can be thought of as bands. While low numbers are accessible  
    at higher tiers, these paths are never the most efficient, and can be 
    ignored. Thus relevant jump-index relationships might include, for example: 

    jumps/tier               0     1       2       3 
    (relevant)indices        0     1 - 2   3 - 6   7 - 14

    Variables: 
    - final_idx (int): Last index in nums and stopping point for the loop
    - tier_limits (list): Lower and upper bounds of indices accessible at this 
                    "tier". Lower bound (exclusive), Upper bound (inclusive)
                    Doesn't include indices already accessible at lower tiers.
    - next_jump_limit (int): Future upper bound of next tier. Initialized as 
                    equal to upper tier limit.
    - jumps (int) - Akin to which tier on the tree, with root at 0 jumps.

    >>> jump_game_ii([2,3,1,1,4])
    2

    >>> jump_game_ii([2,3,0,1,4])
    2

    >>> jump_game_ii([2, 5, 0, 4, 10, 6, 2, 8, 3, 4])
    3
    """

    jumps = 0

    if len(nums) == 1:
        return jumps

    final_idx = len(nums) - 1 
    tier = [-1, 0]
    next_jump_limit = tier[1]  

    # Loop til it returns
    while True:
        # Checks farthest index first in case final_idx, then closer values.
        # Reminder: lower bound of tier tuple is exclusive. 
        for idx in range(tier[1], tier[0], -1): # (2, 0)
            potential_hop = nums[idx] + idx
            if potential_hop >= final_idx:
                return jumps + 1

            if potential_hop > next_jump_limit:
                next_jump_limit = potential_hop

        # move on to next tier
        jumps += 1
        tier = (tier[1], next_jump_limit)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(datetime.datetime.now() - begin_time)