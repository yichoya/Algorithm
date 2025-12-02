import sys
input = sys.stdin.readline

n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
INF = 123456789

# suffix[row][col]: 현재 위치에서 오른쪽 끝까지 걸어가는 비용(누적합)
suffix = [[0]*n for _ in range(n)]
for r in range(n):
    s = 0
    for c in range(n-1, -1, -1):
        s += board[r][c]
        suffix[r][c] = s


min_val = [[INF] * n for _ in range(n)]
for c in range(n):
    min_val[0][c] = suffix[0][c]

for r in range(1, n):
    prev = min_val[r-1]
    cur = min_val[r]
    srow = suffix[r]
    for c in range(n):
        # 현재 행까지의 최소값 = min(위쪽 최소, 현재 suf)
        v = prev[c]
        if srow[c] < v:
            v = srow[c]
        cur[c] = v

for _ in range(q):
    x, y, L = map(int, input().split())
    x -= 1
    y -= 1

    # 1. 점프 안 하는 경우
    ans = suffix[x][y]

    # 2. 점프하는 경우
    limit = x - L
    if limit >= 0:
        suf_x = suffix[x]
        base = suf_x[y]
        mu = min_val[limit]

        for c in range(y, n):
            cost = base - suf_x[c] + mu[c]
            if cost < ans:
                ans = cost

    print(ans)