import sys
input = sys.stdin.readline

d, k = map(int, input().split())

dp = [(0, 0)] * (d+1)
dp[1] = (1, 0)
dp[2] = (0, 1)

for i in range(3, d+1):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

x, y = dp[d]
for a in range(1, k+1):
    if (k - x*a) % y == 0:
        b = (k - x*a) // y
        if b >= 1:
            print(a)
            print(b)
            break
