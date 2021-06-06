import timeit


def potencia(b, e):
    if e == 1:
        return b
    if e == 0:
        return 1
    return b * potencia(b, e - 1)


def pot_eff(b, e):
    # quanto maior o expoente, mais eficiente em relação ao outro codigo
    import math
    if e == 0:
        return 1
    return math.prod((b,) * e)


def pot_eff_2(b, e):
    if e == 0:
        return 1
    product = 1
    i = 0
    while i < e:
        product *= b
        i += 1
    return product


def pot_eff_3(b, e): # postado por leonardofc
    x = 1
    while True:
        t = e % 2
        e = int(e/2)
        if t == 1:
            x = x * b
        if e == 0:
            break
        b = b * b
    return x


inicio = timeit.default_timer()
n1 = potencia(12, 500)
fim = timeit.default_timer()
print('Tempo código do professor: %f' % (fim - inicio))  # Tempo código do professor: 0.000425

inicio = timeit.default_timer()
n2 = pot_eff(12, 500)
fim = timeit.default_timer()
print('Tempo do meu código %f' % (fim - inicio))  # Tempo do meu código 0.000045

inicio = timeit.default_timer()
n3 = pot_eff_2(12, 500)
fim = timeit.default_timer()
print('Tempo do meu código 2 %f' % (fim - inicio))  # Tempo do meu código 0.000045

inicio = timeit.default_timer()
n3 = pot_eff_3(12, 500)
fim = timeit.default_timer()
print('Tempo do meu código 3 %f' % (fim - inicio))  # Tempo do meu código 0.000045


print(potencia(12, 500) == pot_eff(12, 500) == pot_eff_2(12, 500) == pot_eff_3(12, 500))
