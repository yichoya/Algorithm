import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
board = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    if a < b:
        board[a].append([b, c])

dp = [[-1] * (m + 1) for _ in range(n + 1)]
dp[1][1] = 0

for cnt in range(1, m + 1):
    for cur in range(1, n + 1):
        if dp[cur][cnt] == -1:
            continue
        for nxt, happy in board[cur]:
            if cnt + 1 <= m:
                dp[nxt][cnt + 1] = max(dp[nxt][cnt + 1], dp[cur][cnt] + happy)
print(max(dp[n]))