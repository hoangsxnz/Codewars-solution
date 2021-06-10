from math import sqrt

def divisors(n):
    large = []
    stop = int(sqrt(n) + 1)
    for d in range(1, stop):
        if n % d == 0:
             yield d
             if d*d != n:
                 large.append(n // d)
    for d in reversed(large):
        yield d

def yield_squares(m, n):
    for i in range(m, n+1):
        s = sum(map(lambda d: d*d, divisors(i)))
        if sqrt(s).is_integer():
            yield [i, int(s)]

def list_squared(m, n):
    return list(yield_squares(m, n))
