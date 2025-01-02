import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())
# dp[날짜][지각 횟수][연속 결석 횟수]: 현재 상태에서 개근상을 받을 수 있는 경우의 수
dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]

def recur(cur, l, a):
    if l >= 2 or a == 3:
        return 0

    if cur == n:
        return 1

    if dp[cur][l][a] != -1:
        return dp[cur][l][a]

    tmp = 0
    tmp = recur(cur + 1, l, 0) + recur(cur + 1, l + 1, 0) + recur(cur + 1, l, a + 1)
    dp[cur][l][a] = tmp
    return dp[cur][l][a] % 1000000

print(recur(0, 0, 0))