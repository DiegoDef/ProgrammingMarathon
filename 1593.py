for _ in range(int(input())):
    num = list(filter(lambda x: x == "1", str(bin(int(input())))))
    print(num.count("1"))
