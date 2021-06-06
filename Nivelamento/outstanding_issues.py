parenteses = input()
cont = 0
for c in parenteses:
    if c == "(":
        cont += 1
    elif c == ")" and cont > 0:
        if cont > 0:
            cont -= 1
if cont == 0:
    print(f"Partiu RU!")
else:
    print(f"Ainda temos {cont} assunto(s) pendente(s)!")
