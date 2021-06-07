# Os tijolos rotulados aparecem apenas em linhas ímpares, e ocupam posições ímpares dentro das suas linhas.

n = int(input())

for _ in range(n):
    num = []
    impar_total = []
    par_total = []
    par_anterior = []
    for _ in range(5):
        num.append(input().split())
    for n in reversed(num):
        par = []
        impar = []

        for i, j in zip(n, range(5)):
            if j == 0:
                impar.append(i)
                impar.append(0)
            else:
                impar.append(i)
                l = len(impar)
                try:
                    impar.append(par_anterior[l] + par_anterior[l+1])

        impar_total.append(impar)

        if len(impar) > 1:
            quant = 0
            while quant < len(impar) - 1:
                par.append(impar[quant] + impar[quant + 1])
            par_total.append(par)
            par_anterior = par

        print(par_total, impar_total)
