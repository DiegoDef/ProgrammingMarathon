v, t = map(int, input().split())
a = map(int, input().split())
for n in a:
    v += n
    if v > 100:
        v = 100
    elif v < 0:
        v = 0
print(v)
