def quickselect(L, k):
    """finds the the kth biggest item in unseroted list L

    example
    -------
    >>> L = [3, 4, 2, 10, 4, 8, 4, 5]
    >>> # L_sorted = [2, 3, 4, 4, 4, 5, 8, 10]
    >>> # L[8-4]
    >>> quickselect(L, 4) #4th biggest item in L
        4
    """

    # Find the 2nd biggest item
    max_item = max(L[0], L[1])
    penult_item = min(L[0], L[1])

    for i in range(1, len(L)):
        if L[i] > max_item: 
            penult_item = max_item
            max_item = L[i]

        elif L[i] > penult_item:
            penult
    


    return max_item