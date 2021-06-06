hora1, min1, hora2, min2 = map(int, input().split())
tempo_total = [0, 0]

if hora1 < hora2:
    if min1 <= min2:
        tempo_total[0] = hora2 - hora1
        tempo_total[1] = min2 - min1
    else:
        tempo_total[0] = hora2 - hora1 - 1
        tempo_total[1] = 60 - (min1 - min2)
elif hora1 > hora2:
    if min1 <= min2:
        tempo_total[0] = 24 - (hora1 - hora2)
        tempo_total[1] = min2 - min1
    else:
        tempo_total[0] = 23 - (hora1 - hora2)
        tempo_total[1] = 60 - (min1 - min2)
else:
    if min1 <= min2:
        if min1 >= min2:
            tempo_total[0] = 24
            tempo_total[1] = min2 - min1
        else:
            tempo_total[0] = 0
            tempo_total[1] = min2 - min1
    else:
        tempo_total[0] = 23
        tempo_total[1] = 60 - (min1 - min2)

print(f"O JOGO DUROU {tempo_total[0]} HORA(S) E {tempo_total[1]} MINUTO(S)")
