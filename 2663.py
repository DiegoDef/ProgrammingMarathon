from collections import Counter

pontuacoes = []
quant_competidores = int(input())
vagas = int(input())

for _ in range(quant_competidores):
    pontuacoes.append(int(input()))

pontuacoes = Counter(pontuacoes)
dados_ordenados = sorted(pontuacoes.items(), key=lambda ch: ch[0], reverse=True)
quant_classificados = 0

for chave, valor in dados_ordenados:
    quant_classificados += valor
    if quant_classificados >= vagas:
        break
print(quant_classificados)
