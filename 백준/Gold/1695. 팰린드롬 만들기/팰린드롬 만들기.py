import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

def recur():
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):  # 길이가 1인 경우는 항상 팰린드롬임
        for i in range(n - length + 1):
            j = i + length - 1
            if li[i] == li[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
    return dp[0][n - 1]

print(recur())