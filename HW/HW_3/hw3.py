import time

def find_pairs_naive(lst, target):
    """Returns a set of tuples of numbers that add up to the target number"""

    num_set = set()                         #1 
    for i in lst:                           #n (Use of nested for loops that iterates through the list that add up to target)
        for j in lst:                       #n
            if i + j == target and i != j:  #1 (checks for two conditions)
                num_set.add((i, j))         #1
                lst.remove(i)               #1
    return num_set                          #1                                         
                                            #-----------------
                                            # n^2 + 2 = O(n^2)
    #find_pairs_naive is O(n^2) due to the use of nested for loops that iterate through the list twice, which is n^2. Compared to the optimized function, which is O(n), the naive function is much slower.
                

def find_pairs_optimized(lst, target):
    """An optimized version of find_pairs_naive that returns a set of tuples of numbers that add up to the target number"""

    num_set = set()                                           #1
    for i in lst:                                             #n (use of a single for loop that iterates through the list)
        if target - i in lst and i != (target-i):             #1 (subtracts i from target to find other number that adds up to target and makes sure i is not equal to target-i
            num_set.add((i, (target - i)))                    #1 (adds tuple to set)
            lst.remove(i)                                     #1 (removes i from list to prevent duplicates)
    return num_set                                            #1
                                                              #-----------------
                                                              # n + 2 = O(n)

    #find_pairs_optimized is O(n) due to the use of a single for loop that iterates through the list once, which is n thus making it linear. Compared to the naive function, which iterates twice using two for loops, the optimized function is much faster.

def measure_min_time(fn, args):
    """Runs 10 tests of the function fn with the given arguments and returns the minimum time"""

    minimum = float('inf')

    # Run the function 10 times and returns the minimum time 
    for i in range(10):
        start = time.time()
        fn(*args)
        end = time.time()
        # Updates the minimum time if the current time is less than the minimum time
        minimum = (end-start) if (end-start) < minimum else minimum

    return minimum

if __name__ == '__main__':

    print('    n      naive time     optimized')
    print('*' * 37)

    # Run the function with different size lists
    for n in [10, 50, 100, 150, 200, 300, 500, 1000, 5000]:
        lst = [i for i in range(n+1)]
        print(f'{n:5d} {measure_min_time(find_pairs_naive, (lst, n//2)):15.4e} {measure_min_time(find_pairs_optimized, (lst, n//2)):14.4e}')
