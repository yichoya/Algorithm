import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
board = [[1] * (n + 1)] + [[1] + list(map(int, sys.stdin.readline().split())) for _ in range(m)]
sx, sy, sd = map(int, sys.stdin.readline().split())
ex, ey, ed = map(int, sys.stdin.readline().split())

dir_map = {
    1: (0, 1),
    2: (0, -1),
    3: (1, 0),
    4: (-1, 0),
}

def left(d):
    return {1: 4, 4: 2, 2: 3, 3: 1}[d]

def right(d):
    return {1: 3, 3: 2, 2: 4, 4: 1}[d]


visited = [[[False] * 5 for _ in range(n + 1)] for _ in range(m + 1)]

q = deque()
q.append((sx, sy, sd, 0))
visited[sx][sy][sd] = True

while q:
    x, y, d, cnt = q.popleft()

    if (x, y, d) == (ex, ey, ed):
        print(cnt)
        break

    # Go
    dx, dy = dir_map[d]
    for k in range(1, 4):
        nx = x + dx * k
        ny = y + dy * k

        if not (1 <= nx <= m and 1 <= ny <= n):
            break
        if board[nx][ny] == 1:
            break

        if not visited[nx][ny][d]:
            visited[nx][ny][d] = True
            q.append((nx, ny, d, cnt + 1))

    # Turn
    for nd in (left(d), right(d)):
        if not visited[x][y][nd]:
            visited[x][y][nd] = True
            q.append((x, y, nd, cnt + 1))

