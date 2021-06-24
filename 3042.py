while (n := int(input())) != 0:
    obs = []
    jogada = 0
    posicao = 1
    total_de_toques = 0
    for _ in range(n):
        obs.append(list(map(int, input().split())))
    while True:
        if obs[jogada][posicao] == 0:
            jogada += 1
        else:
            i = obs[jogada].index(0)
            if posicao == 0:
                posicao = i
                total_de_toques += posicao
                jogada += 1
            elif posicao == 1:
                total_de_toques += 1
                if i == 0:
                    posicao = 0
                else:
                    posicao = 2
                jogada += 1
            else:
                if i == 0:
                    total_de_toques += 2
                    posicao = 0
                else:
                    total_de_toques += 1
                    posicao = 1
                jogada += 1
        if jogada == n:
            break
    print(total_de_toques)
