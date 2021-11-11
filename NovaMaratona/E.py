def tasks(task1, task2, tempo=0):
    try:
        if tempo == 0:
            tempo = task1[0]

        while True:
            p1 = task1.pop(0)
            if len(task2) > 0:
                if len(task1) == 0:
                    tempo += 10
                if p1 + 10 < task1[0] and task2[0] < task1[0]:
                    tempo += 10
                    return tasks(task2, task1, tempo)
                else:
                    p2 = task1.pop(0)
                    novo_tempo = p2 - p1 + 10
                    if len(task1) > 0:
                        if novo_tempo < task1[0]:
                            tempo += novo_tempo
                        else:
                            tempo += p2 - p1
                            tempo += task1[0] - tempo
                    else:
                        tempo += novo_tempo
            else:
                if len(task1) >= 1:
                    if p1 + 10 < task1[0]:
                        tempo += 10
                        return tasks(task1, [], tempo)
                    else:
                        p2 = task1.pop(0)
                        novo_tempo = p2 - p1 + 10
                        if len(task1) > 0:
                            if novo_tempo < task1[0]:
                                tempo += novo_tempo
                            else:
                                tempo += p2 - p1
                                tempo += task1[0] - tempo
                        else:
                            tempo += novo_tempo
                else:
                    if len(task1) == 1:
                        p2 = task1.pop(0)
                        tempo += p2 - p1 + 10
                    else:
                        tempo += 10

    except IndexError:
        if len(task2) > 0:
            return tasks(task2, [], tempo)
        if len(task1) == 0 and len(task2) == 0:
            print(tempo)


tasks_direita = []
tasks_esquerda = []
count = 0
tempo_total = 0
indo_pra_direita = True

for _ in range(int(input())):
    x, y = map(int, input().split())

    if y == 0:
        tasks_direita.append(x)
    else:
        tasks_esquerda.append(x)
    count += 1

if len(tasks_direita) > 0 and len(tasks_esquerda) > 0:
    if tasks_direita[0] < tasks_esquerda[0]:
        tempo_total = tasks(tasks_direita, tasks_esquerda)
    else:
        tempo_total = tasks(tasks_esquerda, tasks_direita)
elif len(tasks_direita) > 0:
    tempo_total = tasks(tasks_direita, [])
else:
    tempo_total = tasks(tasks_esquerda, [])
