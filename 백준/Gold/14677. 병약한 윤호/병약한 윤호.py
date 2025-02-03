import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
pills = list(sys.stdin.readline().rstrip())
dp = [[[-1] * 3 for _ in range(n*3)] for _ in range(n*3)]
res = 0
# idx 범위는 0, 1, 2
def recur(start, end, idx):
    global res

    if start >= n * 3 or end < 0 or start > end:
        return 0

    if dp[start][end][idx % 3] != -1:
        return dp[start][end][idx % 3]

    char = "BLD"
    tmp = 0
    # 내가 먹어야하는 약봉지의 글자 확인
    if pills[start] == char[idx % 3]:
        tmp = max(tmp, recur(start + 1, end, idx + 1) + 1)
    if pills[end] == char[idx % 3]:
        tmp = max(tmp, recur(start, end - 1, idx + 1) + 1)

    dp[start][end][idx % 3] = tmp
    return dp[start][end][idx % 3]

print(recur(0, 3*n - 1, 0))
