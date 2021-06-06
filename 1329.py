while int(input()) != 0:
    n = list(map(int, input().split()))
    print(f"Mary won {n.count(0)} times and John won {n.count(1)} times")
