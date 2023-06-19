import sys

N, M = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    parent, child, distance = map(int, sys.stdin.readline().split())
    tree[parent].append((child, distance))
    tree[child].append((parent, distance))


def DFS(node, dist):
    for n, d in tree[node]:
        cost = dist + d
        if visited[n] == -1:
            visited[n] = cost
            DFS(n, cost)
    return

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    visited = [-1] * (N + 1)
    visited[a] = 0
    DFS(a, 0)
    print(visited[b])