import sys

n = int(sys.stdin.readline())
wines = []
for _ in range(n):
    wines.append(int(sys.stdin.readline()))

dp = [0] * n

dp[0] = wines[0]

if n >= 2:
    dp[1] = wines[0] + wines[1]
if n>= 3:
    dp[2] = max(dp[1], wines[1] + wines[2], wines[0] + wines[2])
if n >= 4:
    for i in range(3, n):
       dp[i] = max(wines[i] + dp[i - 2], wines[i] + wines[i - 1] + dp[i - 3], dp[i - 1])

print(dp[n - 1])