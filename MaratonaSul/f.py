"""
n = pessoas assistindo
k = visualizações alvo
"""

n, k = map(int, input().split())
tempo = []
soma = []
count = 0
views = 0
inicial = []

for _ in range(n):
    x, y = map(int, input().split())
    tempo.append(x)
    inicial.append(y)
    count = x

quebrar = False
while True:
    for p, index in zip(tempo, range(len(tempo))):
        if p == count:
            tempo[index] += inicial[index]
            views += 1
        if views >= k:
            break
            quebrar = True
    if views >= k or quebrar:
        break
    count += 1

print(count)

