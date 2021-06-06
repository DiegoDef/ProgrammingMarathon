quant = int(input())
i = 0
while i < quant:
    num = []
    qt, s = map(int, input().split())
    num = list(map(int, input().split()))
    if s in num:
        print(num.index(s)+1)
    else:
        rest = [abs(x - s) for x in num]
        print(rest.index(min(rest))+1)
    i += 1
