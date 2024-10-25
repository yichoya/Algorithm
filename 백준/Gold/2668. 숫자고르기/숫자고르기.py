import sys
n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = int(sys.stdin.readline())
    graph[i].append(tmp)
visited = [False] * (n + 1)

def dfs(i, start):
    visited[i] = True
    for nxt in graph[i]:
        if nxt == start:
            arr.append(nxt)
            break
        if visited[nxt]:
            continue
        dfs(nxt, start)
    visited[i] = False

arr = []
for node in range(1, n + 1):
    dfs(node, node)

arr.sort()
print(len(arr))
for a in arr:
    print(a)