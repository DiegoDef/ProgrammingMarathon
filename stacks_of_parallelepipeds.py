# https://www.educamaisbrasil.com.br/enem/matematica/paralelepipedo
for _ in range(int(input())):
    um_no_dois = False
    dois_no_um = False
    dimensoes = list(map(int, input().split()))
    paralel1 = dimensoes[:3]
    paralel2 = dimensoes[3:]
    paralel1.sort()
    paralel2.sort()

    if paralel1[0] < paralel2[1] and paralel1[1] < paralel2[-1]:
        um_no_dois = True
    if paralel2[0] < paralel1[1] and paralel2[1] < paralel1[-1]:
        dois_no_um = True

    if um_no_dois and dois_no_um:
        print("3")
    elif dois_no_um:
        print("2")
    elif um_no_dois:
        print("1")
    else:
        print("0")
