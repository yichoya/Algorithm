import sys
n = int(sys.stdin.readline().rstrip())
l = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(l):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
res = 0

def dfs(node):
    global res
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            res += 1
            dfs(i)

dfs(1)
print(res)