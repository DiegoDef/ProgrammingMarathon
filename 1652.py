l, n = map(int, input().split())
irregular_words = {}
produtos = []
plurais = ("o", "s", "ch", "sh", "x")
vogais = ("a", "e", "i", "o", "u")
for _ in range(l):
    words = input().split()
    irregular_words[words[0]] = words[1]

for _ in range(n):
    produtos.append(input())

for prod in produtos:
    if prod in irregular_words:
        print(irregular_words[prod])
    elif prod.endswith("y") and prod[-2] not in vogais:
        prod = prod[::-1].replace("y", "sei", 1)
        print(prod[::-1])
    elif prod[-1] in plurais or prod[len(prod)-2:] in plurais:
        print(prod + "es")
    else:
        print(prod + "s")
