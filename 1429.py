import math


while (x := input()) != "0":
    n = len(x)
    total = 0
    for num in x:
        total += int(num) * math.factorial(n)
        n -= 1
    print(total)
