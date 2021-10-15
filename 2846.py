index = int(input())
fibonot = []
a = 1
b = 1
cont = 2
while True:
    n = a + b
    a = b
    b = n
    if cont < b:
        for n in range(cont, b):
            fibonot.append(n)
        cont = b
        if len(fibonot) > index:
            print(fibonot[index])
            break
    cont += 1
