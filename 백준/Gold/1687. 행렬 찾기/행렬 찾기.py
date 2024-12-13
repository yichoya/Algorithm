import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0] * (m + 1)] + [[0] + list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = board[i][j] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

ans = 0
for startY in range(1, m + 1):
    for endY in range(startY, m + 1):
        tmp = 0
        for row in range(1, n + 1):
            row_sum = prefix_sum[row][endY] - prefix_sum[row][startY - 1] - prefix_sum[row - 1][endY] + prefix_sum[row - 1][startY - 1]
            if row_sum == 0:
                tmp += (endY - startY + 1)
                ans = max(ans, tmp)
            else:
                tmp = 0
print(ans)