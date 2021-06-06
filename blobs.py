for _ in range(int(input())):
    entrada = float(input())
    count = 0
    while entrada > 1:
        entrada /= 2
        count += 1
    print(f"{count} dias")
