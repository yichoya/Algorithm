import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key=lambda x: x[0])
dp = [[-1] * (10001) for _ in range(n)]

def recur(cur, end):

    if cur == n:
        return 0

    if dp[cur][end] != -1:
        return dp[cur][end]

    tmp1 = 0
    if end <= data[cur][0]:
        tmp1 = recur(cur + 1, data[cur][1]) + data[cur][2]
    tmp2 = recur(cur + 1, end)
    dp[cur][end] = max(tmp1, tmp2)
    return dp[cur][end]

print(recur(0, 0))
