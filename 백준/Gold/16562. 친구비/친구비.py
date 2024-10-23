import sys
sys.setrecursionlimit(10**6)
n, m, k = map(int, sys.stdin.readline().split())
cost = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v, w = map(int, sys.stdin.readline().split())
    graph[v].append(w)
    graph[w].append(v)
visited = [False] * (n + 1)

def dfs(cur):
    global mn_cost

    mn_cost = min(mn_cost, cost[cur])
    visited[cur] = True
    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        dfs(nxt)

res = 0
for i in range(1, n + 1):
    if not visited[i]:
        mn_cost = 1234567890
        dfs(i)
        res += mn_cost

if res > k:
    print("Oh no")
else:
    print(res)