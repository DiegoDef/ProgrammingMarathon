resp = {True: "sim", False: "nao"}
while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    soma = sum(map(int, tuple(str(m))))
    print(soma, resp[soma % 3 == 0])
