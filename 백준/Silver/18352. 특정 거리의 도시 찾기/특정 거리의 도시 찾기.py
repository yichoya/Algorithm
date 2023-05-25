import sys, heapq
INF = int(1e9)

# N:정점 M:간선 K:목표거리 X:시작점
N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited = [False] * (N + 1)
distance = [INF] * (N + 1)

def dijkstra(k, x):
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + 1
            if cost < distance[i]: 
                distance[i] = cost 
                heapq.heappush(q, (cost, i))

dijkstra(K, X)

if K not in distance:
    print(-1)
else:
    for i in range(1, len(distance)): 
        if distance[i] == K:
            print(i)