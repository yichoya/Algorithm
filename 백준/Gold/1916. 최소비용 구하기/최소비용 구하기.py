import sys, heapq
INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
S, E = map(int, sys.stdin.readline().split())

cost = [INF] * (N + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    cost[start] = 0

    while q:
        pay, now = heapq.heappop(q)
        if cost[now] < pay:
            continue

        for i in graph[now]:
            tmp = pay + i[0]
            if tmp < cost[i[1]]:
                cost[i[1]] = tmp
                heapq.heappush(q, (tmp, i[1]))

dijkstra(S)
print(cost[E])