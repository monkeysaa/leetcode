import pprint

def has_word(node, word, kids, node_to_letter, used_letters):
    """Identify whether neighboring nodes contain word

    node(tuple) = row, col, zero-indexed e.g. for (0, 2), row = 0, col = 2

    word(string) = string between 1 and 15 chars
        e.g. 'ABCD' 

    kids(dict) = tuple position that maps to its neighbors (2-4)
        eg. kids[(0, 0)] = [(0, 1), (1, 0)]
        eg. kids[(1, 1)] = [(0, 1), (1, 0), (1, 2), (2, 1)]

    node_to_letter(dict) = (row, col) position tuple with letter as value
        e.g. node_to_letter[(0, 0)] = 'A'
    
    used_letters = lst of nodes for letters in word, to avoid repetition.
        e.g. used_letters = [(0, 0), (0, 1)]
    """
    print(node, kids[node])
    # if node doesn't match next letter in word
    if word[0] != node_to_letter[node]: 
        return False
    
    # if matches last letter in word
    elif word[0] == node_to_letter[node] and len(word) == 1:
        if node in used_letters:
            return False
        else:
            return True
    
    else: #letter matches but it's a longer string, we need to recurse
        used_letters_cp = used_letters.copy() 
        used_letters_cp.append(node)
        for kid in kids[node]:
            if has_word(kid, word[1:], kids, node_to_letter, used_letters_cp):
                return True
        
        return False
        

def exist(board, word):
    """Identify whether a boggle-style word can be found in a grid of letters.

    Given an m x n grid of characters board and a string word, return true if 
    word exists in the grid.
    
    The word can be constructed from letters of sequentially adjacent cells, 
    where adjacent cells are horizontally or vertically neighboring. The same 
    letter cell may not be used more than once.
    
    Solution:
    Create graph with positions as keys. (Positions unique but letters aren't). 
    Then, DFS through graph, following word from start to finish. 
    
    Kids(dict) mapping position as keys to (2-4) neighbor nodes as values
        eg. kids[(0, 0)] = [(0, 1), (1, 0)]
        eg. kids[(1, 1)] = [(0, 1), (1, 0), (1, 2), (2, 1)]
    
    Helper dict
    Node_to_letter(dict) = (row, col) position tuple as key with letter value
        eg. node_to_letter[(0, 0)] = 'A'
    
    Helper functions
    Remove_non_neighbors(potential_neighbors, board) 
        Takes in a list of tuples and removes nodes outside the board bounds.
        Returns nothing
        eg. remove_non_neighbors([(-1, 0), (0, -1), (1, 0), (0, 1)], board)
            Returns nothing, but neighbors reduced to: [(1, 0), (0, 1)]

    Has_word(node, word, kids, node_to_letter, used_letters) does recursive DFS.
        exceptions: 1 letter left is right, next letter wrong, letter repeated
        Returns True if word is found in board, else False.
    """

    kids = {}

    def remove_non_neighbors(potential_neighbors, board):
        """Remove false neighbor nodes that fall beyond board coordinates."""

        print(f"  -> DEBUG: potential neihbors: {potential_neighbors}")
        for node in potential_neighbors:
            print(f"  -> DEBUG: testing {node}: {node[0]} x {node[1]}")
            if not(-1 < node[0] < len(board) and -1 < node[1] < len(board[0])):
                print("   -> removing")
                potential_neighbors.remove(node)
            else:
                print("   -> keeping")

    for i, row in enumerate(board): 
        for j, col in enumerate(row):
            print(f"DEBUG: Test case: {i} x {j}")
            neighbors = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
            print(f"DEBUG: Will test ...")
            pprint.pprint(neighbors)
            remove_non_neighbors(neighbors, board)

            kids[(i, j)] = neighbors

    pprint.pprint(kids)
    
    node_to_letter = {}
    root_nodes = []

    for kid in kids:
        node_to_letter[kid] = board[kid[0]][kid[1]]
        if node_to_letter[kid] == word[0]:
            root_nodes.append(kid)
    
    print(root_nodes)
        
    used_letters = []
    for node in root_nodes:
        if has_word(node, word, kids, node_to_letter, used_letters):
            return True

    return False
    

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))