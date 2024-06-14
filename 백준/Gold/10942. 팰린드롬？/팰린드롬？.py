import sys
n = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 1

for i in range(1, n):
    if nums[i] == nums[i + 1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

for continue_number in range(3, n+1):
    for start in range(n - continue_number + 2):
        end = start + continue_number - 1

        if nums[start] == nums[end] and dp[start + 1][end - 1] == 1:
            dp[start][end] = 1

m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s][e])