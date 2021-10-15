quant_pessoas = [int(input()), int(input()), int(input())]
andar1 = (quant_pessoas[1] + quant_pessoas[2] * 2) * 2
andar2 = (quant_pessoas[0] + quant_pessoas[2]) * 2
andar3 = (quant_pessoas[0] * 2 + quant_pessoas[1]) * 2
local_cafeteira_tempo = [andar1, andar2, andar3]
print(min(local_cafeteira_tempo))
