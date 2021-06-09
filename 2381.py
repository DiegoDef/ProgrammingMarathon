n, k = map(int, input().split())
nomes = []
for _ in range(n):
    nomes.append(input())
nomes.sort()
print(nomes[k-1])
