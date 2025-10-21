import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])
    cnt = 1
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                cnt += 1
    return cnt

res = [0] * (n + 1)
max_cnt = 0

for i in range(1, n + 1):
    res[i] = bfs(i)
    if res[i] > max_cnt:
        max_cnt = res[i]

for i in range(1, n + 1):
    if res[i] == max_cnt:
        print(i, end=' ')
