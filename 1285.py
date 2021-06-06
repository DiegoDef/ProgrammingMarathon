def filt(inicio, final):
    cont = 0
    n = inicio
    while n <= final:
        if sorted(list(str(n))) == sorted(list(set(str(n)))):
            cont += 1
        n += 1
    return cont


while True:
    try:
        n = input().split()
    except EOFError:
        break
    print(filt(int(n[0]), int(n[1])))
