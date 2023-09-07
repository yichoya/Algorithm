import sys
INF = 1e9
n, k = map(int, sys.stdin.readline().split())
unit = []
for _ in range(n):
    unit.append(int(sys.stdin.readline()))

dp = [INF] * (k + 1)
dp[0] = 0

for i in unit:
    for j in range(i, k+1):
        if (j - i >= 0):
            dp[j] = min(dp[j - i] + 1, dp[j])

if (dp[k] == INF): print(-1)
else: print(dp[k])