list = []

for _ in range(int(input())):
    list.append(int(input()))

for n in list:
    soma = 0
    for n2 in range(1, n):
        if n % n2 == 0:
            soma += n2
    if soma == n:
        print(f"{n} eh perfeito")
    else:
        print(f"{n} nao eh perfeito")
