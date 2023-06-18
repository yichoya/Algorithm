import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    parent = tmp[0]
    for i in range(1, len(tmp), 2):
        if tmp[i] == -1:
            continue
        if i % 2 != 0:
            child = tmp[i]
            weight = tmp[i + 1]
        tree[parent].append((child, weight))

def DFS(node, value):
    for n, w in tree[node]:
        cost = value + w
        if visited[n] == -1:
            visited[n] = cost
            DFS(n, cost)
    return

visited = [-1]*(n+1)
visited[1] = 0
DFS(1, 0)

idx = visited.index(max(visited))

visited = [-1]*(n+1)
visited[idx] = 0
DFS(idx, 0)
print(max(visited))