import sys

n = int(sys.stdin.readline().rstrip())

INF = 123456789
# dp[n] = n원을 거슬러 줄 수 있는 최소 동전 개수
dp = [INF] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for coin in [2, 5]:
        if i - coin >= 0 and dp[i - coin] != INF:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[n] if dp[n] != INF else -1)