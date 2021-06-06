def regions(x):
    w = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def columns(x):
        for m in x:
            # print(sorted(m), w)
            if sum(m) != 45 or sorted(m) != w:
                # print("deu ruim column")
                return 1
        return 0

    def vertical(x):
        i = 0
        j = 0
        while j < 9:
            total = []
            while i < 9:
                total.append(x[i][j])
                i += 1
            # print("t=", total)
            if sum(total) != 45 or sorted(total) != w:
                # print(j, total)
                # print("ruim vert")
                return 1
            i = 0
            j += 1
        return 0

    col = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for y, z in zip(x, range(1, 10)):
        # print(z)
        if z < 4:
            col[1] += y[:3]
            col[2] += y[3:6]
            col[3] += y[6:]
        elif z < 7:
            col[4] += y[:3]
            col[5] += y[3:6]
            col[6] += y[6:]
        else:
            col[7] += y[:3]
            col[8] += y[3:6]
            col[9] += y[6:]
    for n in list(col.values()):
        # print(n, sum(n))
        # print(sorted(n), w)
        if sum(n) != 45 or sorted(n) != w:
            # print("deu ruim na região")
            return 1
    return columns(x) + vertical(x)


w = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())
regiao = [[], [], []]

for i in range(n):
    cont = 0
    x = []
    colunas = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for j in range(1, 10):
        num = list(map(int, input().split()))
        for n, u in zip(num, range(1, 10)):
            colunas[u] += n
        # print(regiao)
        x.append(num)
        # print("Soma", sum(num))
        # print(sorted(num), w)
        if sum(num) != 45 or sorted(num) != w:
            # print(num)
            # print("deu ruim na linha")
            cont += 1
            break
    cont += regions(x)
    if cont == 0:
        print(f"Instancia {i + 1}\n"
              f"SIM\n")
    else:
        print(f"Instancia {i + 1}\n"
              f"NAO\n")
