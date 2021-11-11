"""
desde que o número da caixa seja múltiplo do número que identifica o caminhão

"""

while True:
    total = 0
    i, f, n = map(int, input().split())
    numeros_usados = set()
    if sum((i, f, n)) == 0:
        break
    truck = []
    for _ in range(n):
        truck.append(int(input()))
    for t in truck:
        n = set(range(t, f + 1, t)) - numeros_usados
        total += sum(set(range(t, f + 1, t)) - numeros_usados)
        numeros_usados = numeros_usados.union(set(range(t, f + 1, t)) - numeros_usados)
    print(total)
