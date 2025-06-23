import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + files[i - 1]

    # dp[i][j] = i ~ j를 합치는 최소 비용
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = 123456789

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + (prefix_sum[j] - prefix_sum[i - 1])
                dp[i][j] = min(dp[i][j], cost)

    print(dp[1][n])