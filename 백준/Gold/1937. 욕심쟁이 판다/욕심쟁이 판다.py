import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# dp[x][y]: (x, y)에서 시작했을 때 최대로 이동할 수 있는 칸 수
dp = [[-1] * n for _ in range(n)]

def recur(x, y):
    tmp = 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] > board[x][y]:
                if dp[nx][ny] != -1:
                    tmp = max(tmp, dp[nx][ny] + 1)
                else:
                    tmp = max(tmp, recur(nx, ny) + 1)
    dp[x][y] = tmp
    return dp[x][y]

ans = -123456
for i in range(n):
    for j in range(n):
        ans = max(ans, recur(i, j))
print(ans)
