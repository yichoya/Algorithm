import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

dp = a[:]
for i in range(n):
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + a[i]:
            dp[i] = dp[j] + a[i]

print(max(dp))