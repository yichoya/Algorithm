import sys
from collections import deque
input = sys.stdin.readline

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    sheep, wolf = 0, 0

    if board[i][j] == 'o':
        sheep += 1
    elif board[i][j] == 'v':
        wolf += 1

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] != '#':
                q.append((nx, ny))
                visited[nx][ny] = True

                if board[nx][ny] == 'o':
                    sheep += 1
                elif board[nx][ny] == 'v':
                    wolf += 1

    return (sheep, 0) if sheep > wolf else (0, wolf)


r, c = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * (c) for _ in range(r)]
total_sheep, total_wolf = 0, 0

for i in range(r):
    for j in range(c):
        if not visited[i][j] and board[i][j] != '#':
            s, w = bfs(i, j)
            total_sheep += s
            total_wolf += w

print(total_sheep, total_wolf)