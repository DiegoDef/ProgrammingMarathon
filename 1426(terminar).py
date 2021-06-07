# Os tijolos rotulados aparecem apenas em linhas ímpares, e ocupam posições ímpares dentro das suas linhas.

n = int(input())

for _ in range(n):
    num = []
    impar_total = []
    par_total = []
    par_anterior = []
    for _ in range(5):
        num.append(list(map(int, input().split())))
    for n in reversed(num):
        par = []
        impar = []
        print(1)
        for i, j in zip(n, reversed(range(1, 10))):
            #if j % 2 == 1:
            if len(n) == 9:
                impar.append(i)
                impar.append(0)
            else:
                impar.append(i)
                l = len(impar)
                try:
                    impar.append(par_anterior[l] + par_anterior[l+1])
                except IndexError:
                    pass
            #else:

        print(2)
        impar_total.append(impar)

        if len(impar) > 1:
            quant = 0
            while quant < len(impar) - 1:
                try:
                    par.append(impar[quant] + impar[quant + 1])
                except IndexError:
                    pass
                print(2.5)
                quant += 1
            par_total.append(par)
            par_anterior = par

        print(3)

        print(par_total, impar_total)
