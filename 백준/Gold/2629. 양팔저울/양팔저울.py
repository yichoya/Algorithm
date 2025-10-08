import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
M = int(input())
balls = list(map(int, sys.stdin.readline().split()))

MAX_W = 15000
visited = [[False] * (MAX_W + 1) for _ in range(N + 1)]

def dfs(i, diff):
    if visited[i][diff]:
        return
    visited[i][diff] = True

    if i == N:
        return

    w = weights[i]

    dfs(i + 1, diff)           # 추를 안 올림
    dfs(i + 1, diff + w)       # 왼쪽에 올림
    dfs(i + 1, abs(diff - w))  # 오른쪽에 올림


dfs(0, 0)

for b in balls:
    if b > MAX_W:
        print("N", end=' ')
    elif visited[N][b]:
        print("Y", end=' ')
    else:
        print("N", end=' ')
