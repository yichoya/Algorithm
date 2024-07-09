import sys
n = int(sys.stdin.readline().rstrip())
nums = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[0] * (i+1) for i in range(n)]
dp[0][0] = nums[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j-1 < 0:
            dp[i][j] = dp[i-1][j] + nums[i][j]
            continue
        if j + 1 > i:
            dp[i][j] = dp[i-1][j-1] + nums[i][j]
            continue

        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + nums[i][j]

print(max(dp[n-1]))