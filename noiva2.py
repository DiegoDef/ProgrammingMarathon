p, q = map(int, input().split())
temp1 = 60 - p
pessoa = {}
n = set()
for i in range(q):
    t, nome = input().split()
    hora, minuto = t.split(":")
    hora = int(hora)
    minuto = int(minuto)

    if hora == 23:
        if minuto >= temp1:
            temp = p - minuto
            try:
                pessoa[temp]
                pessoa[temp].append(nome)
            except KeyError:
                pessoa[temp] = []
                pessoa[temp].append(nome)
            n.add(temp)
    else:
        if minuto <= p:
            temp = p + minuto
            try:
                pessoa[temp]
                pessoa[temp].append(nome)
            except KeyError:
                pessoa[temp] = []
                pessoa[temp].append(nome)
            n.add(temp)

for i in sorted(n):
    for name in pessoa[i]:
        print(name)
