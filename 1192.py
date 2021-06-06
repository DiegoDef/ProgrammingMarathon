for _ in range(int(input())):
    n1, l, n2 = input()
    n1 = int(n1)
    n2 = int(n2)
    if n1 == n2:
        print(n1 * n2)
    elif l == l.upper():
        print(n2 - n1)
    else:
        print(n1 + n2)
