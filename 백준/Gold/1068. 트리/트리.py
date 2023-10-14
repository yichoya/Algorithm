import sys

def find(node):
    global ans, checked, dNode

    if node == dNode:
        return

    # 연결된 다른 노드가 없다면 해당 노드가 리프
    if len(graph[node]) == 0:
        ans += 1
        return

    # 현재 노드에 연결된 다른 노드 탐색
    for n in graph[node]:
        if checked[n]:
            continue

        checked[n] = True
        find(n)

N = int(sys.stdin.readline().rstrip())
tree = list(map(int, sys.stdin.readline().rstrip().split()))
root = -1
graph = [[] for _ in range(N + 1)]
for node in range(N):
    p = tree[node]

    if p == -1:
        root = node
        continue

    graph[p].append(node)

dNode = int(sys.stdin.readline().rstrip())
graph[dNode] = []

for g in graph:
    if dNode in g:
        g.remove(dNode)

checked = [False for _ in range(N)]
ans = 0

checked[root] = True
find(root)

print(ans)