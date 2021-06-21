n = int(input())
total = 0
for _ in range(n):
    i, j = map(int, input().split())
    total += round(i/j, 8)
if total > 1:
    print("FAIL")
else:
    print("OK")
