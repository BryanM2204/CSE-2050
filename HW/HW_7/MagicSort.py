from math import log2

def linear_scan(L): 
    "Performs linear scans that checks to see whether the list is sorted, reversed, or if there is at most 5 items out of place"

    counter = 0
    # For loop that uses the range of the list to represent the index - compares first number with the next number if they are in order or not
    # updates counter if they are not
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            counter += 1
    
    # Checks to see if list is sorted
    if L == sorted(L):
        return "sorted"

    # Checks to see that the list has at most 5 numbers out of place
    if 0 < counter <= 5 and L != sorted(L, reverse=True): 
        insertionsort(L)
        return "insertion"
    
    # Checks to see if list is sorted in reverse
    elif L == sorted(L, reverse=True): 
        reverse_list(L)
        return "reverse-list"
    
   
    

def reverse_list(L):
    "Takes a list that is already known to be in reverse from linear_scan and splices it to reverse it"

    L = L[::-1]
    return L

def insertionsort(L, left=0, right=None): 
    "Performs an insertion sort, either with the original list from linear_scan or from a sublist from either quicksort or mergesort"
    
    # Sets right to length of list
    if right is None: right = len(L)

    n = right - left
    # nested for loop to iterate through the list that compares two nnumbers next to eachother and switches them depending on size
    for i in range(n):
        for j in range(left+1, right): #Look at the last i items of the list
            if L[j-1] > L[j]: # if the items are out of order
                L[j], L[j-1] = L[j-1], L[j] # switch them
    


def quicksort(L, left=0, right=None, depth=0, algorithms=set()):
    "Performs a quicksort, either with the original list from linear_scan or from a sublist from either quicksort or mergesort"
    
    # updates the algorithm set to reflect use of the quicksort algorithm
    if len(algorithms) == 0:
        algorithms.add('quicksort')

    # with each recursion - updates depth by 1
    depth += 1

    # Sets right to length of list
    if right is None: right = len(L)

    #base case
    if right-left <= 1: return

    # If sublist length is less than or equal to 16, then use insertion sort
    if (right-left) <= 16: 
        # updates algorithms set
        algorithms.add('insertionsort')
        insertionsort(L, left, right)
        return algorithms

    # Checks max recursive depth - if depth exceeds it then it falls back to mergesort
    if (2*(log2(len(L))+1)) < depth: 
        # updates algorithms set
        algorithms.add('mergesort')
        mergesort(L)
        return algorithms

    # use partition method to find the median
    median = partition(L, left, right)
    # recursion to create sublists
    quicksort(L, left, median, depth, algorithms)
    quicksort(L, median+1, right, depth, algorithms)

def partition(L, left, right):
    "Partitions the list in order to find the median for mergesort"

    i = left
    pivot = right-1
    j = pivot-1

    # uses a while loop that checks to see if the left side of the sublist is lesser than the right
    while i < j:
        # find the first big item
        while L[i] < L[pivot]: i += 1

        # find the first small item
        while i < j and L[j] >= L[pivot]: j-=1

        if i < j: L[i], L[j] = L[j], L[i]

    # avoid the edge case of a sorted 2-item list
    if L[pivot] <= L[i]:
        # move pivot to "middle" of list
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    return pivot



def mergesort(L): 
    """Sorts L in-place using mergesort"""
    ### Base Case ##
    if len(L) < 2:
        return

    ### Divide ###
    median = len(L) // 2
    
    # creats a splice of the left till before the median
    A = L[:median]
    # creates a splice of the median to the right end of the list
    B = L[median:]

    # recrusively calls on mergesort to sort the lists
    mergesort(A)
    mergesort(B)

    ### Conquer ###
    # merge left and right lists
    merge(L, A, B)

def merge(L, Lleft, Lright):
    "merges the left and right lists created from mergesort"
    i, j = 0, 0

    # while loop that checks the counters i and j 
    while i < len(Lleft) and j < len(Lright):
        # makes a comparison and updates the counter i or j
        if Lleft[i] < Lright[j]:
            L[i+j] = Lleft[i]
            i += 1
        else:
            L[i+j] = Lright[j]
            j += 1
    
    # combines the lists
    L[i+j:] = Lleft[i:] + Lright[j:] 
   
def magic_sort(L, depth=0): 
    "sorts L in-place and returns a set with all the sorting algorithms used"

    algorithms = set()
    scan = linear_scan(L)
    # checks the result from linear_scan - if it is not None, then it adds to the set
    if scan is not None:
        algorithms.add(scan)
    # if the list is not sorted and has five more items out of place, then it uses quicksort
    else:
        quicksort(L, algorithms=algorithms)
        
    # returns the algorithm set
    return algorithms
