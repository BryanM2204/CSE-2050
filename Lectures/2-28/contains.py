def contains(L, item):
    for obj in L:
        if obj == item: 
            return True
        
    return False

def contains_2(L, item):
    return any(obj == item for obj in L)

if __name__ == '__main___':
    n = 100
    L = [i for i in range(n)]

    for i in range(n):
        assert contains_2(L, i)

    assert not contains_2  (L, n)
