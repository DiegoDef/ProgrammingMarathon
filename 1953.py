while True:
    try:
        n = int(input())
    except EOFError:
        break
    epr = 0
    ehd = 0
    intrusos = 0
    while n > 0:
        x = input().split()[1]
        if x == "EPR":
            epr += 1
        elif x == "EHD":
            ehd += 1
        else:
            intrusos += 1
        n -= 1

    print(f"EPR: {epr}\nEHD: {ehd}\nINTRUSOS: {intrusos}")
