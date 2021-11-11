from math import gcd

def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n // gcd(m, n)
    return m

N = int(input())
q = N * 2
p = range(N+1, q+1)
result = mmc(p)
print(result)
