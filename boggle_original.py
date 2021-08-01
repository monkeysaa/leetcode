def has_word(node, word, kids, node_to_letter, used):
    # e.g. has_word((0, 0), 'ABCD', kids, letters)
    # node (tuple), e.g. (0, 0)
    # word (string), e.g. "ABCD"
    # kids = tuple position that maps to its neighbors (2-4)
            # kids[(0, 0)] = [(0, 1), (1, 0)]
            # kids[(1, 1)] = [(0, 1), (1, 0), (1, 2), (2, 1)]
    # node_to_letter = {}
        # (0, 0): A, (0, 1): B, (0, 2): C
    # used = set of position-tuples, e.g. if "C" cycle of ABC, used={(0, 0), (0, 1)}"
    # cycle through node's kids and use DFS to see if you can make word

    # break-out cases:
    if node in used:
        return False
    
    if word == node_to_letter[node]:
        return True
    
    elif word[0] != node_to_letter[node][0]:
        return False
    
    # success case:
    else:
        used_children = used.copy()
        used_children.add(node)
        for kid in kids[node]:
            if has_word(kid, word[1:], kids, node_to_letter, used_children):
                return True
            
    return False
            
    
    

def exist(board, word):
    """DFS through graph. If there are two A's, 2 graphs? Or one master node.

    Build graph in its entirety. 
    
    Graph: 
    DFS needs unique keys for nodes & list of child-nodes.
    Letters not unique; Only position unique. 
    Each node has 2- 4 children. 
    
    kids(dict) = tuple position that maps to its neighbors (2-4)
        kids[(0, 0)] = [(0, 1), (1, 0)]
        kids[(1, 1)] = [(0, 1), (1, 0), (1, 2), (2, 1)]
    
    nodes_to_letters(dict) -- shortcut for readability
        (0, 0): 'A', (0, 1): 'B'
    
    Step1. Make kid dict
    """
    
    kids = {}
    
    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            position = (i, j)
            potential_neighbors = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
            neighbors = []
            for neighbor in potential_neighbors:
                row_idx = neighbor[0]
                col_idx = neighbor[1]
                if len(board )> row_idx >= 0 and len(board[0]) > col_idx >= 0: 
                    neighbors.append(neighbor)
            kids[position] = neighbors
    
    node_to_letter = {}
    # (0, 0): A, (0, 1): B, (0, 2): C
    for kid in kids: 
        node_to_letter[kid] = board[kid[0]][kid[1]]
            
    for node in node_to_letter:
        used = set()
        if has_word(node, word, kids, node_to_letter, used):
            return True
    
    return False 
    