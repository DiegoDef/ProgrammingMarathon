def menor_proximo(num):
    def is_prime(n):
        import math

        if n % 2 == 0 and n > 2:
            return False
        return all(n % x for x in range(3, int(math.sqrt(n)) + 1, 2))

    while not is_prime(num):
        num -= 1
    return num


n, m = map(int, input().split())
print(menor_proximo(n) * menor_proximo(m))
