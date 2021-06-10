from math import *

def find_Kprimes(n):
    res, factor = [], 2
    while factor <= int(floor(sqrt(n))):
        while n % factor == 0:
            n /= factor
            res.append(factor)
        factor += 1
    if (n > 1): res.append(n)
    return len(res)
def count_Kprimes(k, start, nd):
    Kprimes = []
    for i in range (start,nd+1):
        if find_Kprimes(i) == k:
            Kprimes.append(i)
    return Kprimes
    
def puzzle(s):
    a = count_Kprimes(1, 0, s)
    b = count_Kprimes(3, 0, s)
    c = count_Kprimes(7, 0, s)
    count = 0
    ia = 0
    while (ia < len(a)):
        ib = 0
        while (ib < len(b)):
            ic = 0
            while (ic < len(c)):
                if (a[ia] + b[ib] + c[ic] == s):
                    count += 1
                ic += 1
            ib += 1
        ia += 1
    return count
