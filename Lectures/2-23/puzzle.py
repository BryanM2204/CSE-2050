def solve_puzzle(board, idx, visited):
    # at some point, update my visited set
    #initialize
    if visited is None: visited = set()

    visited.add(idx)

    # base case
    if idx == len(board) - 1: return True

    # find all valid moves
    idx_cw = (idx + board[idx]) % len(board)
    idx_ccw = (idx - board[idx]) % len(board)
    valid_moves = [idx_cw, idx_ccw]

    #explore valid movies
    for move in valid_moves:
        if move in visited: continue

        path_optimum = solve_puzzle(board, move, visited)
        if path_optimum: return True

    return False

    # for each valid move:
        # find optimum result for that move
        # if that's better than our current best, update

    # return best choice