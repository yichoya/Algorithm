import sys
n, k = map(int, sys.stdin.readline().split())
things = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * 100001 for _ in range(n)]

def recur(cur, w):
    global things
    if w > k:
        return -123123123
    if cur == n:
        return 0
    if dp[cur][w] != -1:
        return dp[cur][w]
    dp[cur][w] = max(recur(cur + 1, w + things[cur][0]) + things[cur][1], recur(cur + 1, w))
    return dp[cur][w]

print(recur(0, 0))