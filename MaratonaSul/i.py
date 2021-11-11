"""
desde que o número da caixa seja múltiplo do número que identifica o caminhão

"""
while True:
    total = 0
    i, f, n = map(int, input().split())
    if sum((i, f, n)) == 0:
        break
    truck = []
    for _ in range(n):
        truck.append(int(input()))
    for t in truck:
        num = set(range(0, f + 1, t))
        outro_num = set(filter(lambda x: x % t == 0, num))
        total += sum(outro_num)
        num = num.difference(outro_num)
    print(total)


