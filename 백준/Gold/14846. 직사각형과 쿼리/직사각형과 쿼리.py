import sys

n = int(sys.stdin.readline())
board = [[0] * (n + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = int(sys.stdin.readline())

# 각 숫자에 대해 누적합 배열
# prefix[num][i][j]: (1,1) ~ (i, j)에서 num이 등장한 횟수
prefix = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(11)]

# 누적합 배열 초기화
for num in range(1, 11):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            val = 1 if board[i][j] == num else 0
            prefix[num][i][j] = prefix[num][i - 1][j] + prefix[num][i][j - 1] - prefix[num][i - 1][j - 1] + val


for _ in range(q):
    x, y, xx, yy = map(int, sys.stdin.readline().split())
    cnt = 0
    for num in range(1, 11):
        total = prefix[num][xx][yy] - prefix[num][x - 1][yy] - prefix[num][xx][y - 1] + prefix[num][x - 1][y - 1]
        if total > 0:
            cnt += 1
    print(cnt)

