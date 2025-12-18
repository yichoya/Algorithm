import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [list(map(int, input().split())) for _ in range(n)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time, last_cheese = 0, 0

while 1:
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    melt = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dxy[i][0], y + dxy[i][1]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

                # 외부 공기와 닿은 치즈인 경우
                elif board[nx][ny] == 1:
                    visited[nx][ny] = True
                    melt.append((nx, ny))

    # 더 이상 녹일 치즈가 없으면 종료
    if not melt:
        break

    last_cheese = len(melt)

    for x, y in melt:
        board[x][y] = 0

    time += 1

print(time)
print(last_cheese)