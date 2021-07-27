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

    Variables: 
    - final_idx (int): Last index in nums and stopping point for the loop
    - visited (set): A set of indices already visited, to avoid repetition.
    - tier (list): Nums indices accessible at this "tier" 
    - next_tier (list): Same
    - jumps (int) - The number of jumps is akin to which tier on the tree.

    >>> jump_game_ii([2,3,1,1,4])
    2

    >>> jump_game_ii([2,3,0,1,4])
    2

    >>> jump_game_ii([2, 5, 0, 4, 10, 6, 2, 8, 3, 4])
    3
    """

    final_idx = len(nums) - 1 
    jumps = 0

    if final_idx == 0:
        return jumps

    tier = [0]
    next_tier = []
    visited = {0}

    # Loop til it returns
    while True:

        for idx in tier:
            # Pop from end of stack (to check first if goal reached)
            node_value = nums[idx] # node_value = 2

            for i in range(node_value, 0, -1):
                hop_idx = idx + i
                if hop_idx >= final_idx:
                    return jumps + 1
                elif hop_idx in visited:
                    pass
                else:
                    visited.add(hop_idx)
                    next_tier.append(hop_idx)

        # move on to next set
        jumps += 1
        tier = next_tier
        next_tier = []




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(datetime.datetime.now() - begin_time)