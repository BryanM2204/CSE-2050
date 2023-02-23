def solve_puzzle(L, index=0, visited=None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    if visited is None: visited = set()
    # 1) Base case: have you found a valid solution?
    if index == len(L) - 1: return True
    visited.add(index)

    # 2) Find all valid next-steps
    next_moves = set()
    
    # set that contains the index of the next move and the index of the previous move
    moves = [index+L[index], index-L[index]]
    
    # for loop that iterates through moves set and adds the move to next_moves if it is not in visited
    for move in moves:
        move %= len(L)
        if move not in visited:
            next_moves.add(move)

    # 3) Recursively explore next-steps, returning True if any valid solution is found
    return any(solve_puzzle(L, move, visited) for move in next_moves)