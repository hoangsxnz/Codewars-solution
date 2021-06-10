def sum_for_list(lst):
    factors = list({factor for value in lst for factor in range(2, abs(value)+1) if value % factor == 0})
    prime = list({i for i in factors if [j for j in range(2,i) if i % j == 0] == []})
    return [[p, sum(e for e in lst if e % p == 0)] for p in sorted(prime)]
