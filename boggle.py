import pprint

def has_word(node, word, kids, node_to_letter, used_letters):
    """Identify whether neighboring nodes contain word
    
    exceptions: 1 letter left is right, next letter wrong

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
    
    if word[0] != node_to_letter[node]: 
        return False
    
    elif word[0] == node_to_letter[node] and len(word) == 1:
        if node in used_letters:
            return False
        else:
            return True
    
    else: #letter matches but it's a longer string, we need to recurse
        print(f'Recurse: {node}')
        new_used = used_letters.copy() 
        new_used.append(node)
        for kid in kids[node]:
            if has_word(kid, word[1:], kids, node_to_letter, new_used):
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
    DFS through graph. If there are two A's, 2 graphs? Or one master node.
    
    Nodes need position & value, and letter not unique. Only position unique. 
    Each node has at most 4 children. 
    Build graph in its entirety. 
    
    Step1. Make kids dict to identify neighbors
        kids(dict) = tuple position that maps to its neighbors (2-4)
        kids[(0, 0)] = [(0, 1), (1, 0)]
        kids[(1, 1)] = [(0, 1), (1, 0), (1, 2), (2, 1)]

    Step2. Make a node_to_letter dict
        node_to_letter(dict) = (row, col) position tuple with letter as value

    Step3. Build recursive has_word()
        has_word(node, word, kids, node_to_letter, used_letters)
        account for exceptions: 1 letter left is right, next letter wrong
    """

    kids = {}

    def find_neighbors(potential_neighbors, board):
        """Return only those neighbors within the bounds of board."""

        neighbors = []
        for node in potential_neighbors:
            if -1 < node[0] < len(board) and -1 < node[1] < len(board[0]):
                neighbors.append(node)
        return neighbors

    for i, row in enumerate(board): 
        for j, col in enumerate(row):
            true_neighbors = find_neighbors(
                [(i, j-1), (i, j+1), (i-1, j), (i+1, j)],
                board,
            )

            kids[(i, j)] = true_neighbors
    
    node_to_letter = {}
    root_nodes = []

    for kid in kids:
        node_to_letter[kid] = board[kid[0]][kid[1]]
        if node_to_letter[kid] == word[0]:
            root_nodes.append(kid)
    
    used_letters = []
    for node in root_nodes:
        if has_word(node, word, kids, node_to_letter, used_letters):
            return True

    return False
    

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))