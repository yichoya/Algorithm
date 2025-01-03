import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 현재 집에서 선택할 수 있는 최소 비용 리턴
def recur(cur, prev, start_color):
    if cur == n:
        if prev == start_color:
            return 1234567890
        return 0

    if dp[cur][prev][start_color] != -1:
        return dp[cur][prev][start_color]

    res = 1234567890
    for i in range(3):
        if prev == i: continue
        res = min(res, recur(cur + 1, i, start_color) + rgb[cur][i])

    dp[cur][prev][start_color] = res
    return dp[cur][prev][start_color]

result = 1234567890
for start_color in range(3):
    dp = [[[-1] * 3 for _ in range(3)] for _ in range(n)]
    result = min(result, recur(1, start_color, start_color) + rgb[0][start_color])

print(result)