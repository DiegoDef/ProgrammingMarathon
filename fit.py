n = int(input())
i = 0
for _ in range(n):
    num1 = input()
    num2 = input()
    l1 = len(num1)
    l2 = len(num2)
    if num1[l1-(l1-l2)-1:] == num2:
        print("encaixa")
    else:
        print("nao encaixa")
    i += 1
