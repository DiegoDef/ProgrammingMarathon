en = input().split(" ")
num1 = float(en[0])
num2 = float(en[1])
pib = 100.000000
pib1 = pib + (pib * (num1/100.000000))
pib2 = pib1 + (pib1 * (num2/100.000000))
total = (pib2 - pib)
print(f"{total:.6f}")
