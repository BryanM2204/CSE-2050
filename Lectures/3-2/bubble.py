def is_sorted(L):
    return not any(L[i] > L[i + 1] for i in range(len(L)-1))

def bubble(L):
    'sorts L in-place using bubblesort'
    n = len(L)

    for i in range(n-1):
        keep_going = False
        for j in range(n-1-i):
            if L[j] > L[j+1]: # if two items are out of order
                keep_going = True
                L[j+1], L[j] = L[j], L[j+1] #switch them 

        if not keep_going: break


# Bubble is adaptive - it is asymptotically better
# on some inputs w/o degrading performance on other inputs

# bubble is only adaptive to big items ('rabbits')
# small items near the end move slowly ('turtles')

if __name__ == '__main__':
    assert is_sorted([1, 2, 3])
    assert not is_sorted([3, 2, 1])

    L = [5, 4, 3, 2, 1]
    assert not is_sorted(L)
    bubble(L)
    assert is_sorted(L)

    n = 1000
    L = [i for i in range(n)]
    L[-1] = -1
    print('Starting...')
    bubble(L)
    print('Done')
    assert is_sorted(L)

    L.sort() # in-place sort
    L2 = sorted(L) # returns a new, sorted list