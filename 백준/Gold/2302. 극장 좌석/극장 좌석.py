import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vip = [int(input()) for _ in range(M)]

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = 1
prev = 0
for v in vip:
    length = v - prev - 1
    ans *= dp[length]
    prev = v

ans *= dp[N - prev]

print(ans)