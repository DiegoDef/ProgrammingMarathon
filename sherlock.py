while int(input()) != 0:
    p = tuple(map(int, input().split()))
    o = list(p)
    o.remove(max(o))
    print((p.index(max(o))+1))

