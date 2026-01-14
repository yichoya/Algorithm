import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = board[0][0]

# 첫 번째 행, 열 채우기
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + board[0][j]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + board[i][0]

for x in range(1, n):
    for y in range(1, m):
        dp[x][y] = max(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]) + board[x][y]

print(dp[n - 1][m - 1])