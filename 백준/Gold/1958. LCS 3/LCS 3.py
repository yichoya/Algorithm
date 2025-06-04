import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()

la, lb, lc = len(A), len(B), len(C)
dp = [[[0] * (lc + 1) for _ in range(lb + 1)] for _ in range(la + 1)]

for i in range(1, la + 1):
    for j in range(1, lb + 1):
        for k in range(1, lc + 1):
            if A[i - 1] == B[j - 1] == C[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(
                    dp[i - 1][j][k],
                    dp[i][j - 1][k],
                    dp[i][j][k - 1]
                )

print(dp[la][lb][lc])
