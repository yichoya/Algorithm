import sys
# sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 탑다운
dp = [-1234567890] * 1500051
# dp[i]: i번째 날부터 상담을 시작했을 때 얻을 수 있는 최대 이익
dp[n] = 0
for i in range(n - 1, -1, -1):
    dp[i] = max(dp[i + arr[i][0]] + arr[i][1], dp[i + 1])
print(dp[0])