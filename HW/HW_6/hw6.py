# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L):
    'Finds the index of the zero in the list'
    # base case - item not in list
    if len(L) == 0: return -1

    #base case: found item
    median = (len(L) - 1) // 2
    if L[median] == 0: return median

    #item is in smaller half
    elif L[median] > 0: return find_zero(L[:median])

    # item is in larger half
    else: 
        index = find_zero(L[median+1:])
        if index is False: 
            return False
        else:
            return median + 1 + index
    

def bubble(L, left, right):
    'sorts list from left and right indices using bubblesort'
    # for loop to go through list and perform bubble sort 
    for i in range(right - left -1):
        keep_going = False
        for j in range(left, right-1):
            # Checks to see if two items are out of order
            if L[j] > L[j+1]:
                keep_going = True
                # switches items
                L[j+1], L[j] = L[j], L[j+1]

        if not keep_going: break

def selection(L, left, right):
    'Sorts spliced list from left and right indices using selection sort'
    # for loop to go through list and perform selection sort
    for i in range(right - left - 1):
        min_index = left + i 
        # For loop keeps track of max_index of j 
        for j in range(left+i, right):  
            if L[j] < L[min_index]:  
                min_index = j        
        # Switches items
        L[left+i], L[min_index] = L[min_index], L[left+i] 

def insertion(L, left, right):
    'Sorts list from left and right indices using insertion sort'
    # for loop to go through list and perform insertion sort
    for i in range(right - left):
        for j in range(left+1, right): #Look at the last i items of the list
            if L[j-1] > L[j]: # if the items are out of order
                L[j], L[j-1] = L[j-1], L[j] # switch them
 
def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half