import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time = 0

while 1:
    visited = [[False] * m for _ in range(n)]
    q = deque()
    melt = []
    cnt = [[0] * m for _ in range(n)]

    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue

            if board[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
            else:
                cnt[nx][ny] += 1
                if cnt[nx][ny] >= 2:
                    melt.append((nx, ny))

    if not melt:
        break

    for i, j in melt:
        board[i][j] = 0

    time += 1

print(time)