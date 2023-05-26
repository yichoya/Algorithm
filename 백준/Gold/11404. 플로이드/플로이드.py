import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for z in range(1, n + 1):
            graph[y][z] = min(graph[y][z], graph[y][x] + graph[x][z])

for r in range(1, n + 1):
    for c in range(1, n + 1):
        if graph[r][c] == INF:
           print(0, end=" ")
        else:
            print(graph[r][c], end=" ") 
    print()