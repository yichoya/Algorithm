import sys

n = int(sys.stdin.readline())
square_nums = [i * i for i in range(1, 316)]
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    if i in square_nums:
        dp[i] = 1
    else:
        tmp = [dp[i - j] for j in square_nums if i - j > 0]
        dp[i] = min(tmp) + 1
        # print(tmp)
print(dp[n])