import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0] * (m + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
ans = -1e9
# 누적합 배열 채우기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + board[i][j]
# 모든 사각형을 탐색하면서 최댓값 찾기
for startX in range(1, n + 1):
    for startY in range(1, m + 1):
        for endX in range(startX, n + 1):
            for endY in range(startY, m + 1):
                square_sum = prefix_sum[endX][endY] - prefix_sum[endX][startY - 1] - prefix_sum[startX - 1][endY] + prefix_sum[startX - 1][startY - 1]
                ans = max(ans, square_sum)
print(ans)