def selection_sort(L):
    for i in range(len(L) - 1):
        max_index = 0
        for j in range(len(L) - i):  #Next 3 lines select
            if L[j] > L[max_index]:  #
                max_index = j        #
        L[-1-i], L[max_index] = L[max_index], L[-1-i] # sorts