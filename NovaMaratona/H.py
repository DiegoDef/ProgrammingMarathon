n, k = map(int, input().split())
ordered = []
unordered = []
unordered_d = {}
list_y = []
passa = True

for _ in range(n):
    x, y = map(int, input().split())
    ordered.append(x)
    unordered.append(x)
    list_y.append(y)
ordered.sort()

for num in ordered:
    esta_agr = list_y[unordered.index(num)]
    deve_estar = list_y[ordered.index(num)]

    if esta_agr != deve_estar:
        passa = False
        break

if passa:
    print("Y")
else:
    print("N")
