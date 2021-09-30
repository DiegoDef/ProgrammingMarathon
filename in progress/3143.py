total_caracter = int(input())

linhas = []
while True:
    try:
        entrada = input()
    except EOFError:
        break
    linhas.append(entrada)

# desconsiderar espaço no começo da linha
linhas_cortadas = []
total_de_linhas = 0
for x in linhas:
    while True:
        nova_linha = x[:total_caracter]
        x = x.replace(nova_linha, "")
        linhas_cortadas.append(nova_linha)
        #print(nova_linha)
        try:
            while x[0] == " ":
                x = x[1:]
        except IndexError:
            pass
        #print(x)
        if x == "":
            break
    #print("D", len(linhas_cortadas))
print(len(linhas_cortadas))
