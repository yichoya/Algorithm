import sys, copy
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
mars = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
dp = [[0] * m for _ in range(n)]    # dp[x][y] = (x, y) 까지 왔을 때 가능한 최대 가치 저장

# 첫 줄은 접근 가능한 방향이 한 가지
dp[0][0] = mars[0][0]
for i in range(1, m):
    dp[0][i] = dp[0][i - 1] + mars[0][i]

for i in range(1, n):
    ltor = [0] * m    # 왼쪽, 위쪽에서 오는 경우
    rtol = [0] * m    # 오른쪽, 위쪽에서 오는 경우
    for j in range(m):
        # 첫번째 칸은 그냥 갱신
        if j == 0:
            ltor[j] = mars[i][j] + dp[i - 1][j]
            rtol[m - 1 - j] = mars[i][m - 1 - j] + dp[i - 1][m - 1 - j]
            continue

        ltor[j] = mars[i][j] + max(dp[i - 1][j], ltor[j - 1])
        rtol[m - 1 - j] = mars[i][m - 1 - j] + max(dp[i - 1][m - 1 - j], rtol[m - j])

    # ltor, rtol 중 최대값 저장
    tmp = [max(ltor[i], rtol[i]) for i in range(m)]
    dp[i] = copy.deepcopy(tmp)

print(dp[n - 1][m - 1])