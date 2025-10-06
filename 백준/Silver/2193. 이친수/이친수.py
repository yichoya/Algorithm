import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
dp = [[-1] * 2 for _ in range(n + 1)]

def recur(cur, last):
    if cur == 1:
        if last == 0:
            return 0
        return 1

    if dp[cur][last] != -1:
        return dp[cur][last]

    if last == 0:
        dp[cur][last] = recur(cur - 1, 0) + recur(cur - 1, 1)
    else:
        dp[cur][last] = recur(cur - 1, 0)

    return dp[cur][last]



print(recur(n, 0) + recur(n, 1))