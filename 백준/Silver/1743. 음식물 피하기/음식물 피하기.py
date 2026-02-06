import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [['.'] * m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = '#'


def bfs(q):
    sz = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    sz += 1
    return sz

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * m for _ in range(n)]
ans = -12345
for i in range(n):
    for j in range(m):
        if board[i][j] == '#' and not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True
            ans = max(ans, bfs(q))

print(ans)