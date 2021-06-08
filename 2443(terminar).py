def soma_fracao(a, b, c, d):
    if b == d:
        divisor = b
        dividendo = a + c
    else:
        divisor = b * d
        a = a * (divisor / b)
        c = c * (divisor / d)
        dividendo = a + c
    return dividendo, divisor


def menor_possivel(e, f):
    primos = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    for num in primos:
        dividendo = e / num
        divisor = f / num
        if e % num == 0 and e % num == 0:
            e = dividendo
            f = divisor
        m = min(e, f)
        if num > (m / 2)+1:
            return e, f


a, b, c, d = map(int, input().split())
pri, seg = soma_fracao(a, b, c, d)
e, f = menor_possivel(pri, seg)
print(int(e), int(f))
