"""Se a palavra está na lista de palavras irregulares substitua-a com o plural dado.
Senão se a palavra termina em uma consoante seguida por "y", substitua "y" por "ies".
Senão se a palavra termina em "o", "s", "ch", "sh" ou "x", acrescente "es" à palavra.
Senão acrescente "s" à palavra."""

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
    elif prod in plurais:
        print(prod + "es")
    else:
        print(prod + "s")
