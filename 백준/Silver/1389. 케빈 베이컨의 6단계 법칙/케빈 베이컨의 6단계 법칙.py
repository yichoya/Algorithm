import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
gragh = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    gragh[a].append(b)
    gragh[b].append(a)


def bfs(i):
    visited = [0] * (N+1)
    queue.append(i)
    visited[i] = 1
    while queue:
        t = queue.popleft()
        for v in gragh[t]:
            if not visited[v]:
                visited[v] = visited[t]+1
                queue.append(v)
    return sum(visited)

queue = deque()
res = []
for i in range(1, N+1):
    res.append(bfs(i))

print(res.index(min(res))+1)