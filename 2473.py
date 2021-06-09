x = input().split()
y = input().split()
premio = {3: "terno", 4: "quadra", 5: "quina", 6: "sena"}
cont = 0
for n in x:
    if n in y:
        cont += 1
if cont > 2:
    print(premio[cont])
else:
    print("azar")
