while True:
    matriz = []
    linha_1 = 0
    linha_2 = 0
    total = 0
    try:
        i, j = map(int, input().split())
    except EOFError:
        break
    for n in range(i):
        array = list(map(int, input().split()))
        matriz.append(array)
        if 1 in array and 2 in array:
            linha_1 = n
            linha_2 = n
        else:
            if 1 in array:
                linha_1 = n
            elif 2 in array:
                linha_2 = n
    total = abs(linha_1 - linha_2)
    total += abs(matriz[linha_1].index(1) - matriz[linha_2].index(2))
    print(total)
