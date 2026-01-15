import sys
input = sys.stdin.readline

n = int(input().rstrip())
board = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: (0, 0)에서 (i, j)까지 도달 가능한 경우의 수
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if (i == n - 1 and j == n - 1):
            continue

        val = board[i][j]
        if j + val < n:
            dp[i][j + val] += dp[i][j]

        if i + val < n:
            dp[i + val][j] += dp[i][j]

print(dp[n - 1][n - 1])