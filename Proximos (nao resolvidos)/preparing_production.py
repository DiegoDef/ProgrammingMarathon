# -*- coding: utf-8 -*-
while True:
    try:
        quant_pacotes = int(input())
    except EOFError:
        break
    tempo_total = 0
    num_pacotes = list(map(int, input().split()))
    num_inicial = tuple(num_pacotes.copy())
    tempo_substituir = list(map(int, input().split()))
    tempo_substituir = dict(zip(num_pacotes, tempo_substituir))
    for n in num_inicial:
        index = num_pacotes.index(n)
        if index > n - 1:
            # num_pacotes = [1, 2, 3, 4, 5, 6]
            for num in num_pacotes[n:index]:
                tempo_total += tempo_substituir[num]
            quant_deslocadas = abs(n - 1 - index)
            tempo_total += tempo_substituir[n] * quant_deslocadas
            removido = num_pacotes.pop(index)
            num_pacotes.insert(n - 1, removido)
        elif index < n - 1:
            for num in num_pacotes[index+1:n]:
                tempo_total += tempo_substituir[num]
            quant_deslocadas = abs(n - 1 - index)
            tempo_total += tempo_substituir[n] * quant_deslocadas
            removido = num_pacotes.pop(index)
            num_pacotes.insert(n - 1, removido)
    print(tempo_total)


"""

while True:
    try:
        quant_pacotes = int(input())
    except EOFError:
        break
    tempo_total = 0
    num_pacotes = list(map(int, input().split()))
    tempo_substituir = list(map(int, input().split()))
    for n in num_pacotes:
        while n != num_pacotes[n - 1]:
            index = num_pacotes.index(n)
            removido = num_pacotes.pop(index)
            if index < n - 1:
                tempo_total += tempo_substituir[index]
                tempo_total += tempo_substituir[index + 1]
                num_pacotes.insert(index + 1, removido)
                removido_tempo = tempo_substituir.pop(index)
                tempo_substituir.insert(index + 1, removido_tempo)
            else:
                tempo_total += tempo_substituir[index]
                tempo_total += tempo_substituir[index - 1]
                num_pacotes.insert(index - 1, removido)
                removido_tempo = tempo_substituir.pop(index)
                tempo_substituir.insert(index + 1, removido_tempo)
    print(tempo_total)

"""
