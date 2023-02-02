import time

def time_function(func, args, n_trials=10):
    """Returns the time it takes to run func(args)"""
    
    minimum = float('inf')

    #For loop created that iterates i amount of times, where i is the number of trials
    for i in range(n_trials):
        start = time.time()
        func(args)
        end = time.time()
        
        #finds the minimum by comparing the current time to the previous minimum
        minimum = (end-start) if (end-start) < minimum else minimum

    return minimum

def time_function_flexible(func, args, n_trials=10):
    """Returns the time it takes to run func(args) with multiple parameters"""
    minimum = float('inf')

    for i in range(n_trials):
        start = time.time()
        func(*args)
        end = time.time()
        
        minimum = (end-start) if (end-start) < minimum else minimum

    return minimum

if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        """Test function to see if time_function works"""
        for item in L:
            item *= 2

    def test_func_flexible(L1, L2, L3):
        """Test function to see if time_function_flexible works using multiple parameters with *args"""
        for item in L1:
            item *= 2
        for item in L2:
            item *= 2
        for item in L3:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    L3 = [i for i in range(10**7)] # should be 100x slower to operate on every item
    t3 = time_function_flexible(test_func_flexible, (L1, L2, L3))

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))
    print("t(L3) = {:.3g} ms".format(t3*1000))