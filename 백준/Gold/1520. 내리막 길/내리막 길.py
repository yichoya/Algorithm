import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cnt = 0

def recur(x, y):
    global cnt

    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if board[nx][ny] >= board[x][y]:
            continue

        dp[x][y] += recur(nx, ny)
        
    return dp[x][y]

print(recur(0, 0))