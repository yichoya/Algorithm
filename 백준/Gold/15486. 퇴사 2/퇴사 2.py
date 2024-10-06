import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [-1] * n

def recur(cur): # 앞으로 최적의 상담을 골랐을 때의 수익 리턴
    if cur > n:
        return -100000000
    if cur == n:
        return 0
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    return dp[cur]

print(recur(0))