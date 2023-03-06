def greedy_fewest_coins(amt, coins):
    # sort coins in reverse order
    coins.sort(reverse=True)
    
    # initialize num coins
    num_coins = 0

    for coin in coins:
        num_coins += amt // coin # 63//25 = 2
        amt = amt % coin        #63 % 25 = 13

    return num_coins

def dyn_fewest_coins(amt, coins):
    solved = [None]*(amt+1)

    for prob in solved:
        solved[prob] = prob

        for coin in coins:
            if coin <= prob:
                potential_min = 1 + solved[prob-coin]
                if potential_min < solved[min]:
                    solved[min] = potential_min

    return solved[amt]

def recr_fewest_coins(amt, coins, solved=None):
    #base case - amt is one of my coins
    if solved is None: 
        solved = {coin:1 for coin in coins}

    if amt in solved: return solved[amt]

    # Initialize "worst case optimum"
    min_coins = amt #assuming we have pennies

    #find all valid next steps
    valid_coins = [coin for coin in coins if coin<=amt]

    #explore all next steps, keeping track of best solution
    for coin in valid_coins:
        if amt-coin not in solved: 
            path_optimum = 1 + recr_fewest_coins(amt-coin, coins, solved)
            if path_optimum < min_coins:
                min_coins = path_optimum
    
    #after for loop, return the optimal solution
    solved[amt] = min_coins
    
    return solved[amt]

    # Explore every branch to find the branch optimum
    # if that branch optimum is better than our current opt: update
    for coin in coins:
        if coin < amt: #this is a valid step
            path_optimum = 1 + recr_fewest_coins(amt-coin, coins)
            if path_optimum < min_coins: min_coins = path_optimum

    return min_coins
counter = 0
print(recr_fewest_coins(77, [1]))
print(recr_fewest_coins(80, [1]))
print(recr_fewest_coins(63, [1, 5, 10, 21, 25, 30, 31, 32]))