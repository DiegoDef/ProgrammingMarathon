def main():

    H = {}
    m = {}
    p, q = input().split()
    p = int(p)
    q = int(q)

    for i in range(q):
        t, n = input().split()
        H[n] = t
        hora, minuto = t.split(":")
        if int(hora) == 23:
            minuto = (60 - int(minuto))
        else:
            t = "24:{}".format(minuto)
        if int(minuto) > p:
            continue

        if int(hora) == 23:
            m[n] = int(minuto) + 60
        else:
            m[n] = int(minuto) + 120

    res = {k: v for k, v in sorted(m.items(), key=lambda item: item[1])}
    res2 = {}
    for k, v in res.items():
        res2[k] = H[k]

    res3 = {k: v for k, v in sorted(res2.items(), key=lambda item: item[1])}
    for k, v in res2.items():
        print(k)

main()