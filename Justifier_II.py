entradas_quant = 1
ja_executado = False
while entradas_quant != 0:
    entradas_quant = int(input())
    if entradas_quant != 0 and ja_executado:
        print()
    linha_de_texto = []
    quant_maior = 0
    linha_justificada = []
    for n in range(entradas_quant):
        linha_de_texto.append(list(input().split()))
        linha_de_texto[n] = " ".join(linha_de_texto[n])
        if len(linha_de_texto[n]) > quant_maior:
            quant_maior = len(linha_de_texto[n])
    for n in range(len(linha_de_texto)):
        while len(linha_de_texto[n]) < quant_maior:
            linha_de_texto[n] = " " + linha_de_texto[n]
        print(linha_de_texto[n])
    ja_executado = True
