import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[1] = True
def bfs(cur):
    q = deque([(cur, 0)])
    cnt = 0
    while q:
        cur, depth = q.popleft()
        if depth >= 2:
            continue
        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append((nxt, depth + 1))
                visited[nxt] = True
                cnt += 1
        depth += 1
    return cnt

print(bfs(1))