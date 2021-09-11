while (n := input().split()) != ['0', '0']:
    start, end = map(int, n)
    cont_n = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    numero = 1
    while start <= end:
        for num in str(start):
            cont_n[num] += 1
        start += 1
    cont = 0
    for r in cont_n.values():
        if cont < 9:
            print(r, end=" ")
        else:
            print(r)
        cont += 1

# com problemas de otimição. Time limit exceeded
