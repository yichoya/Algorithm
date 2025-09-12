import sys
sys.setrecursionlimit(10**6)

c, n = map(int, sys.stdin.readline().rstrip().split())
data = list(tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))

dp = [-1] * (c + 1)
ans = 12345
# 현재 people명일 때 c명을 넘기기까지 필요한 최소 비용을 리턴하는 함수
def recur(people):
    global ans

    if people >= c:
        return 0

    if dp[people] != -1:
        return dp[people]

    tmp = 123456789
    for cost, cnt in data:
        tmp = min(tmp, cost + recur(people + cnt))

    dp[people] = tmp
    return dp[people]

print(recur(0))