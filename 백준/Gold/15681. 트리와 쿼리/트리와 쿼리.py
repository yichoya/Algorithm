import sys
sys.setrecursionlimit(10**6)

n, r, q = map(int, sys.stdin.readline().rstrip().split())
trees = [[] for _ in range(n + 1)]
sz = [-1 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split(' '))
    trees[a].append(b)
    trees[b].append(a)

def dfs(cur, sz):
    sz[cur] = 1
    for nxt in trees[cur]:
        if sz[nxt] == -1:
            sz[cur] += dfs(nxt, sz)  # nxt 노드의 서브트리 개수 더하기
    return sz[cur]  # cur 노드의 서브트리 개수 리턴

dfs(r, sz)

for _ in range(q):
    x = int(sys.stdin.readline().rstrip())
    print(sz[x])