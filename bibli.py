while True:
    l = []
    try:
        n = int(input())
    except EOFError:
        break
    cont = 0
    while cont < n:
        l.append(input())
        cont += 1
    l.sort(key=lambda x: int(x))
    for t in l:
        print(t)

