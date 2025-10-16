import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
    global cnt

    visited[cur] = True
    cnt += 1
    ans[cur] = cnt

    for nxt in board[cur]:
        if not visited[nxt]:
            dfs(nxt)

    return


n, m, r = map(int, input().rstrip().split())
board = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    board[a].append(b)
    board[b].append(a)

for i in range(1, n + 1):
    board[i].sort()

visited = [False] * (n + 1)
ans = [0] * (n + 1)
cnt = 0

dfs(r)
for i in range(1, n + 1):
    print(ans[i])