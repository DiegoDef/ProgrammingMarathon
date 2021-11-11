n, c, t = map(int, input().split())
familias = {}
for _ in range(c):
    x, y, z = input().split()

    if z in familias:
        familias[z].extend([x, y])
    else:
        familias[z] = [x, y]

    if x in familias:
        familias[z] += familias[x]
    else:
        familias[x] = []

    if y in familias:
        familias[z] += familias[y]
    else:
        familias[y] = []

for _ in range(t):
    x, y = input().split()

    f1 = set(familias[x])
    f2 = set(familias[y])

    if len(f1.intersection(f2)) > 0:
        print("verdadeiro")
    else:
        print("falso")
