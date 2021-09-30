linhas = []
while True:
    try:
        entrada = input()
    except EOFError:
        break
    linhas.append(entrada)
index = []
h1 = False
for x, y in zip(linhas, range(len(linhas))):
    if "<body>" in x:
        h1 = True
    elif h1 and "</body>" not in x:
        index.append(y)
    elif "</body>" in x:
        break

for n in index:
    print(linhas[n])
