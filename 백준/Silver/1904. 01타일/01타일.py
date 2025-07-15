n = int(input())
MOD = 15746

dp = [0] * (n + 2)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[n])