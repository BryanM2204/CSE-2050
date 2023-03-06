def bs(L, item):
    #base case: L is empty
    if len(L) == 0: return False

    median = len(L) // 2

    if L[median] == item: return True

    elif L[median] < item: return bs(L[median+1:], item)

    elif L[median] > item: return bs(L[0:median], item)

    

if __name__ == '__main__':
    n = 128
    L = [i for i in range(n)]

    for i in range(n):
        assert bs(L, i)
    
    assert not bs(L, n)