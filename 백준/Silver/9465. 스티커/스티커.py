import sys
sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline().rstrip())

def recur(cur, prev):
    if cur == n + 1:
        return 0

    if dp[cur][prev] != -1:
        return dp[cur][prev]

    max_res = recur(cur + 1, 2)
    if prev != 0:
        max_res = max(max_res, recur(cur + 1, 0) + sticker[0][cur])

    if prev != 1:
        max_res = max(max_res, recur(cur + 1, 1) + sticker[1][cur])

    dp[cur][prev] = max_res
    return dp[cur][prev]



for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    sticker = []
    for _ in range(2):
        tmp = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
        sticker.append(tmp)

    dp = [[-1] * 3 for _ in range(n + 2)]
    print(recur(1, 2))