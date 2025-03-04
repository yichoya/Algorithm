import sys

n = int(sys.stdin.readline())
line = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
line.sort(key=lambda x: x[0])

dp = [1] * n
for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))