def factorial(x):
    'returns factorial of x'

    #type validation
    if not isinstance(x, int):
        raise TypeError(f'Cannot calculate factorial of type {x.__class__}')

    product = 1

    while x > 1:
        product *= x
        x -= 1

    return product

# Unit test 1 - expected inputs
assert factorial(5) == 120
assert factorial(6) == 720

# Edge case - 0
assert factorial(0) == 1

# Unit test 2 - input validation
# Edge case - unexpected types
# How do I catch an exception

try:
    factorial(2.3)
    raise AssertionError('factorial(2.3) did not raise a TypeError')

except TypeError:
    pass