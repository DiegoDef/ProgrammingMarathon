while sum((num := list(map(int, input().split())))) != 0:
    n, m = num
    x = list(map(int, input().split()))
    quant = {}
    cont = 0
    for i in x:
        if i in quant:
            quant[i] += 1
        else:
            quant[i] = 1
    for i, j in quant.items():
        if j > 1:
            cont += 1
    print(cont)
