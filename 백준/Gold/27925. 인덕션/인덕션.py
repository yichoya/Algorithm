import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
food = list(map(int, sys.stdin.readline().split()))
# 현재 상태에서 마지막 음식까지 요리하는데 드는 최소 비용(?) 저장
dp = [[[[-1] * n for _ in range(10)] for _ in range(10)] for _ in range(10)]

def recur(cur, f1, f2, f3):
    if cur == n:
        return 0

    if dp[f1][f2][f3][cur] != -1:
        return dp[f1][f2][f3][cur]

    tmp = 1234567890
    tmp = min(tmp, recur(cur + 1, food[cur], f2, f3) + min(abs(10 - abs(food[cur] - f1)), abs(food[cur] - f1)))
    tmp = min(tmp, recur(cur + 1, f1, food[cur], f3) + min(abs(10 - abs(food[cur] - f2)), abs(food[cur] - f2)))
    tmp = min(tmp, recur(cur + 1, f1, f2, food[cur]) + min(abs(10 - abs(food[cur] - f3)), abs(food[cur] - f3)))

    dp[f1][f2][f3][cur] = tmp
    return dp[f1][f2][f3][cur]

print(recur(0, 0, 0, 0))