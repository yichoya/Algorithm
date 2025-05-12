import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    #dp[i][j][k]: 길이가 i이고, j개의 인접한 비트를 갖고, 마지막 비트가 k인 수열의 개수
    dp = [[[0 for _ in range(2)] for _ in range(101)] for _ in range(101)]
    dp[1][0][0] = 1
    dp[1][0][1] = 1

    for i in range(2, 101):
        for j in range(101):
            # 마지막 비트가 0: 이전 수열의 끝이 0이든 1이든, 0을 붙여고 인접한 비트의 개수는 늘어나지 않음
            dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]

            # 마지막 비트가 1인 경우
            if j > 0:
                dp[i][j][1] = dp[i - 1][j][0] + dp[i - 1][j - 1][1]
            else:    # j가 0인 경우
                dp[i][0][1] = dp[i - 1][0][0]

    print(dp[n][k][0] + dp[n][k][1])
