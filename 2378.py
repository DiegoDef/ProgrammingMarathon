n, c = map(int, input().split())
atual = 0
limite_ultrapassado = False

for _ in range(n):
    s, e = map(int, input().split())
    atual += e - s
    if atual > c:
        limite_ultrapassado = True
        break
if limite_ultrapassado:
    print("S")
else:
    print("N")
