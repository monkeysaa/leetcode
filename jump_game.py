def jump_game_ii(nums):
    """LeetCode #45: https://leetcode.com/problems/jump-game-ii/

    Given an array of non-negative integers nums, you are initially positioned 
    at the first index of the array.
    
    Each element in the array represents your max jump length at that position.
    Your goal is to reach the last index in the minimum number of jumps.
    You can assume that you can always reach the last index.

    >>> jump_game_ii([2,3,1,1,4])
    2

    >>> jump_game_ii([2,3,0,1,4])
    2

    """

    length = len(nums)

    if length == 1:
        return 0
    
    #graph {index:[]}
    graph = {}
    traceback = {}
    for index, num in enumerate(nums[:-1]):
        graph[index] = []

        for j in range(1, num+1):
            graph[index].append(index+j)
            if index+j == length-1:
                # set up traceback, using recursive function
                break
        
    """
    for i, n in enumerate(nums[:-1]):
        graph[i] = []
        for j in range(i+1, i+n+1):
            if j >= len(nums): break
            graph[i].append(j)
    # {0: [1, 2], 1: [2, 3, 4], 2: [3], 3: [4]} 
     """
    
    print(graph)

    boundary = graph[0] #1, 2
    hops = 0

    while True: # TODO
        print(boundary)
        new_boundary = []
        for n in boundary: 
            new_boundary.extend(graph[n])
        print(f'new {new_boundary}')
        if (len(nums) - 1) in new_boundary:
            return hops + 1
        hops += 1
        boundary = new_boundary
    

if __name__ == "__main__":
    jump_game_ii([2,3,1,57, 2, 4])