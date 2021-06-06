soma = 0
x = 0
while True:
    try:
        input()
        n = int(input())
    except EOFError:
        break
    soma += n
    x += 1
media = soma / x
print(round(media, 1))
