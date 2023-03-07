def insertion_sort(L):
    for i in range(len(L)):
        for j in range(len(L)-i, len(L)): #Look at the last i items of the list
            if L[j-1] > L[j]: # if the items are out of order
                L[j], L[j-1] = L[j-1], L[j] # switch them