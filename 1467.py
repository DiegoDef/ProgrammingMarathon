n = ("A", "B", "C", "*")
while True:
    try:
        x = list(map(int, input().split()))
    except EOFError:
        break

    c1 = x.count(1)
    c0 = x.count(0)
    s = sum(x)

    if s == 3 or s == 0:
        print("*")
    elif c1 < c0:
        print(n[x.index(1)])
    elif c0 < c1:
        print(n[x.index(0)])
