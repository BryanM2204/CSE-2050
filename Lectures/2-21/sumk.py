import timeit
import sys

sys.setrecursionlimit(2000)

def sumk(k):
    temp_sum = 0

    for i in range(1, k+1):
        temp_sum += 1
    
    return temp_sum

def sumk_recr(k):
    if k in {0, 1}: return k
    return k + sumk_recr(k-1)

def factorial(n):
    if n in {0, 1}: return 1
    return n * factorial(n-1)


#Fibonacci sequence
#every item is equual to the sum of the two previous items
#1, 1, 2, 3, 5, 8, 13,...
def fibonacci(n):
    return _fibonacci(n, {1:1, 2:1})

def _fibonacci(n, solved={}):
    global counter
    counter += 1

    # if solved is None:
    #     solved = dict()
    #     solved[1] = 1
    #     solved[2] = 1

    if n in solved: return solved[n]

    solved[n] = _fibonacci(n-1, solved) + _fibonacci(n-2, solved)

    return solved[n]

counter = 0
    # if n in {1, 2}: return 1
    #base case:
    #   1:1
    #   2:1
    #   3:2
    #   4:3
    #   5:5

print(fibonacci(100))
print(f'counter = {counter}')

print(factorial(10))
print(sumk_recr(1000))

# for func in [sumk_recr, sumk]:
#         t = timeit.timeit(f'{func.__name__}(20)', globals=globals())
#         print(f"{func.__name__}: {t:.3g} s")

#sumk(k) = k + (k-1) + (k-2) + ... + 2 + 1
#sumk(k) = k + sumk(k-1)
#               k-1 + sumk(k-2)
#                       k-2 + sumk(k-3)
#                               ...