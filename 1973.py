input()
index = 1
estrelas_atacadas = set()
stars = list(map(int, input().split()))
stars.append(None)
stars.insert(0, None)
while True:
    if stars[index] is not None and stars[index] > 0:
        estrelas_atacadas.add(index)
        if stars[index] % 2 == 1:
            stars[index] -= 1
            index += 1
        else:
            stars[index] -= 1
            index -= 1
    else:
        break
print(len(estrelas_atacadas), sum(stars[1:-1]))
