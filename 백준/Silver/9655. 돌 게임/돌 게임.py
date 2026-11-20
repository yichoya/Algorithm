import sys

input = sys.stdin.readline
n = int(input().strip())

dp = [False] * (n + 4)
dp[1] = True
dp[2] = False
dp[3] = True

for i in range(4, n + 1):
    if not dp[i - 1] or not dp[i - 3]:
        dp[i] = True
    else:
        dp[i] = False

print("SK" if dp[n] else "CY")