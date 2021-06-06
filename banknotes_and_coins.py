notas = (100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01)
contagem = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.50: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}

valor = float(input())
for n in notas:
    while valor - n >= 0:
        valor -= n
        contagem[n] += 1
        valor = round(valor, 2)

print(f"NOTAS:\n"
      f"{contagem[100]} nota(s) de R$ 100.00\n"
      f"{contagem[50]} nota(s) de R$ 50.00\n"
      f"{contagem[20]} nota(s) de R$ 20.00\n"
      f"{contagem[10]} nota(s) de R$ 10.00\n"
      f"{contagem[5]} nota(s) de R$ 5.00\n"
      f"{contagem[2]} nota(s) de R$ 2.00\n"
      f"MOEDAS:\n"
      f"{contagem[1]} moeda(s) de R$ 1.00\n"
      f"{contagem[0.5]} moeda(s) de R$ 0.50\n"
      f"{contagem[0.25]} moeda(s) de R$ 0.25\n"
      f"{contagem[0.10]} moeda(s) de R$ 0.10\n"
      f"{contagem[0.05]} moeda(s) de R$ 0.05\n"
      f"{contagem[0.01]} moeda(s) de R$ 0.01")
