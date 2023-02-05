import time

def find_pairs_naive(lst, target):
    """"""
    num_set = set()
    for i in lst:
        for j in lst:
            if i + j == target and i != j:
                num_set.add((i, j))
                lst.remove(i)

    return num_set

                

def find_pairs_optimized(lst, target):
    """"""
    num_set = set()
    for i in lst:
        if target - i in lst:
            num_set.add((i, (target - i)))
            lst.remove(i)

    return num_set


def measure_min_time(fn, args):
    """"""
    minimum = float('inf')

    for i in range(10):
        start = time.time()
        fn(*args)
        end = time.time()

        minimum = (end-start) if (end-start) < minimum else minimum

    return minimum

if __name__ == '__main__':

    print('    n      naive time     optimized')
    print('*' * 37)
    for n in [10, 50, 100, 150, 200, 300, 500, 1000, 5000]:
        lst = [i for i in range(n+1)]
        print(f'{n:5d} {measure_min_time(find_pairs_naive, (lst, n//2)):15.4e} {measure_min_time(find_pairs_optimized, (lst, n//2)):14.4e}')
