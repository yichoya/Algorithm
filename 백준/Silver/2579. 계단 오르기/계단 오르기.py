import sys

n = int(sys.stdin.readline().rstrip())
scores = [0] + list(int(sys.stdin.readline().rstrip()) for _ in range(n))
dp = [0] * (n + 1)
dp[1] = scores[1]

if n >= 2:
    dp[2] = scores[1] + scores[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + scores[i - 1]) + scores[i]
print(dp[n])