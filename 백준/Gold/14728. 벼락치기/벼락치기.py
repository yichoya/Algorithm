import sys

n, t = map(int, sys.stdin.readline().rstrip().split())
info = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [0] * (t + 1)
for i in range(n):
    for time in range(t, -1, -1):
        if time - info[i][0] >= 0:
            dp[time] = max(dp[time], dp[time - info[i][0]] + info[i][1])

print(dp[t])