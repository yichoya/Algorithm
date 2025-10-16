import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
subjects = [tuple(map(int, input().rstrip().split())) for _ in range(k)]

dp = [0] * (n + 1)

for imp, time in subjects:
    for t in range(n, time - 1, -1):
        dp[t] = max(dp[t], dp[t - time] + imp)

print(dp[n])