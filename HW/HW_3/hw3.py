def find_pairs_naive(lst, target):

    num_set = set()
    for i in lst:
        for j in lst:
            if i + j == target and i != j:
                num_set.add((i, j))
                lst.remove(j)

    return num_set

                

# def find_pairs_optimized():

print(find_pairs_naive([6, 5, 2, 8, 9, 1], 7))
