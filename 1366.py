while (x := int(input())) != 0:
    total = 0
    for _ in range(x):
        n = int(input().split()[1])
        n = int(n / 2)
        total += n
    print(int(total / 2))
