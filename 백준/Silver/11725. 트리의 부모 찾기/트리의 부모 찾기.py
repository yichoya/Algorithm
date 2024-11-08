import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
gragh = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    gragh[a].append(b)
    gragh[b].append(a)

def dfs(cur, prev):
    parent[cur] = prev
    for nxt in gragh[cur]:
        if nxt == prev:
            continue
        dfs(nxt, cur)

dfs(1, 0)
for i in range(2, n + 1):
    print(parent[i])