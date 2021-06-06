import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % x for x in range(3, int(math.sqrt(n))+1, 2))


for _ in range(int(input())):
    a = int(input())
    if is_prime(a):
        print("Prime")
    else:
        print("Not Prime")
