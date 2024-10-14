import sys
n, k = map(int, sys.stdin.readline().split())
stuff = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * 100001 for _ in range(n)]

def recur(cur, weight):    # cur에서 선택할 수 있는 최대 가치 리턴

    if weight > k:
        return -1234567890
    if cur == n:
        return 0
    if dp[cur][weight] != -1:
        return dp[cur][weight]

    dp[cur][weight] = max(recur(cur + 1, weight), recur(cur + 1, weight + stuff[cur][0]) + stuff[cur][1])
    return dp[cur][weight]

print(recur(0, 0))