import sys
sys.setrecursionlimit(10**7)

n, m = map(int, sys.stdin.readline().split())
gragh = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    gragh[a].append(b)
    gragh[b].append(a)
visited = [False] * (n + 1)
cnt = 0

def dfs(x):
    visited[x] = True
    for i in gragh[x]:
        if visited[i] == False:
            dfs(i)

for i in range(1, n + 1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)