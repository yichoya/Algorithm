import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

def recur(x, y):
    if x < 0 or y < 0:
        return -12345

    if x == 0 and y == 0:
        return board[0][0]

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = max(recur(x - 1, y), recur(x, y - 1), recur(x - 1, y - 1)) + board[x][y]
    return dp[x][y]

recur(n - 1, m - 1)
print(dp[n-1][m-1])