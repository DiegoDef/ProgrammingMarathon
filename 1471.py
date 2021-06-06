while True:
    cont = 0
    try:
        n, r = map(int, input().split())
    except EOFError:
        break
    p_ret = list(map(int, input().split()))
    p = list(range(1, n+1))
    if n != r:
        for i in p_ret:
            p.remove(i)
        print(*p, "")
    else:
        print("*")
