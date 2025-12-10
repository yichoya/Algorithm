import sys
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
INF = 1234567890
dist = [[INF] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

answer = INF
for x in range(1, v + 1):
    answer = min(answer, dist[x][x])

print(answer if answer < INF else -1)
