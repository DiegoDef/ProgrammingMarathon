n, m = map(int, input().split())
jog_total = 0
for _ in range(n):
    partidas = input().split()
    if partidas.count("0") == 0:
        jog_total += 1
print(jog_total)
