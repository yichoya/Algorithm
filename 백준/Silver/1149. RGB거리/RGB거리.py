import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * 3 for _ in range(n)]

def recur(cur, prev):    # 현재 집에서 선택할 수 있는 최소 비용 리턴

    if cur == n:
        return 0
    if dp[cur][prev] != -1:
        return dp[cur][prev]

    res = 1234567890
    for i in range(3):
        if prev != i:
            res = min(res, recur(cur + 1, i) + rgb[cur][i])
    dp[cur][prev] = res
    return dp[cur][prev]

print(recur(0, -1))