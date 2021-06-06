def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


n, e = map(int, input().split())
graph = {}
for _ in range(e):
    a, b = input().split()
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

array1 = find_shortest_path(graph, 'Entrada', '*')
array1.remove("Entrada")
array2 = find_shortest_path(graph, '*', 'Saida')
array2.remove("*")
numero = len(array1) + len(array2)
print(numero)
