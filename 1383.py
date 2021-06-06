def vertical(x):
    i = 0
    j = 0
    while j < 9:
        total = 0
        while i < 9:
            total += x[i][j]
            i += 1
        #print("t=", total)
        if total != 45:
            print(j, total)
            print("ruim vert")
            return 1
        i = 0
        j += 1
    return 0


n = int(input())
for i in range(n):
    cont = 0
    x = []
    regiao = [[], [], []]
    colunas = [[], [], [], [], [], [], [], [], []]
    for j in range(1, 10):
        num = list(map(int, input().split()))
        regiao[0] += num[:3]
        regiao[1] += num[3:6]
        regiao[2] += num[6:]
        #print(regiao)
        x.append(num)
        #print(sum(num))
        if sum(num) != 45:
            #print(num)
            cont += 1
            break

    if cont == 0:
        cont += vertical(x)
        soma = []
        for index in range(3):
            total1 = sum(regiao[index][:9])
            #print(regiao[index][0:9])
            total2 = sum(regiao[index][9:18])
            total3 = sum(regiao[index][18:])
            #print(total1, total2, total3)
            if total1 != 45 or total2 != 45 or total3 != 45:
                print("ruim")
                cont = 1
    if cont == 0:
        print(f"Instancia {i+1}\n"
              f"SIM\n")
    else:
        print(f"Instancia {i + 1}\n"
              f"NAO\n")
