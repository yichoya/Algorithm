import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)

if n > 1:
    dp[2] = 3

    if n >= 4:
        for i in range(4, n + 1):
            if i % 2 == 0:
                dp[i] += dp[i - 2] * 3

                for j in range(i - 4, -1, -2):
                    dp[i] += dp[j] * 2
            
                dp[i] += 2 

print(dp[n])