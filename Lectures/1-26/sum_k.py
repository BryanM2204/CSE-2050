def sum_k(x):
    
    if not isinstance(x, int):
        raise TypeError(f"Can not raise for type {x.__class__}")

    temp_sum = 0

    while x > 0:
        temp_sum += x
        x -= 1

    return temp_sum

assert sum_k(1) == 1
assert sum_k(2) == 3
assert sum_k(3) == 6
assert sum_k(4) == 10

#Edge case 0
assert sum_k(0) == 0

try:
    sum_k(2.2) 
    raise AssertionError('did not raise TypeError')

except TypeError:
    pass
