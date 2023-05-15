import sys

n, k = map(int, sys.stdin.readline().split())
unit = []
for _ in range(n):
    unit.append(int(sys.stdin.readline()))

dp = [0] * (k + 1)
dp[0] = 1
for i in unit:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])