# 0.010s (0.046s), 0.145s (0.083s)

pontuacoes = []
quant_competidores = int(input())
vagas = int(input())

for _ in range(quant_competidores):
    pontuacoes.append(int(input()))
pontuacoes.sort(reverse=True)

quant_classificados = vagas
n_pontuacoes = pontuacoes[vagas:]
x = pontuacoes[vagas-1]

if x in n_pontuacoes:
    quant_classificados += n_pontuacoes.count(x)

print(quant_classificados)
