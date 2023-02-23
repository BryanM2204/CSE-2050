def greedy_fewest_coins(amt, coins):
    # sort coins in reverse order
    coins.sort(reverse=True)
    
    # initialize num coins
    num_coins = 0

    for coin in coins:
        num_coins += amt // coin # 63//25 = 2
        amt = amt % coin        #63 % 25 = 13

    return num_coins


def recr_fewest_coins(amt, coins):
    #base case - amt is one of my coins
    if amt in coins: return 1

    # Initialize "worst case optimum"
    min_coins = amt #assuming we have pennies

    # Explore every branch to find the branch optimum
    # if that branch optimum is better than our current opt: update
    for coin in coins:
        if coin < amt: #this is a valid step
            path_optimum = 1 + recr_fewest_coins(amt-coin, coins)
            if path_optimum < min_coins: min_coins = path_optimum

    return min_coins
    
print(recr_fewest_coins(77, [1]))
print(recr_fewest_coins(80, [1]))
print(recr_fewest_coins(63, [1, 5, 10, 21, 25, 30, 31, 32]))