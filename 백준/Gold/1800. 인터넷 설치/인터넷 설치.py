import sys
from collections import deque

input = sys.stdin.readline
n, p, k = map(int, input().split())

max_cost = 0
graph = [[] for _ in range(n + 1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_cost = max(max_cost, c)


def can_go(X):
    INF = 10**9
    dist = [INF] * (n + 1)
    dist[1] = 0

    q = deque([1])

    while q:
        cur = q.popleft()
        for nxt, cost in graph[cur]:
            extra = 1 if cost > X else 0
            if dist[nxt] > dist[cur] + extra:
                dist[nxt] = dist[cur] + extra
                if extra == 0:
                    q.appendleft(nxt)
                else:
                    q.append(nxt)

    return dist[n] <= k


left, right = 0, max_cost
answer = -1

while left <= right:
    mid = (left + right) // 2
    if can_go(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)