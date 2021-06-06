import math


def karatsuba(u, v, n):
    import math

    if u <= 3 or v <= 3:
        return u * v

    m = n // 2
    _10_m = math.pow(10, m)
    p = u // _10_m
    q = u % _10_m
    r = v // _10_m
    s = v % _10_m

    pr = karatsuba(p, r, m)
    qs = karatsuba(q, s, m)
    y = karatsuba(p + q, r + s, m + 1)
    uv = pr * math.pow(10, 2 * m) + (y - pr - qs) * _10_m + qs

    return uv


a, b, n, k = map(int, input().split())
x = a + math.sqrt(b)
fat = x
fat = karatsuba(123456789, 123456789, 6)
print(fat)



