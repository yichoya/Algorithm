import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = list(input().split() for _ in range(n))
visited = [[False] * m for _ in range(n)]
res = [[0] * m for _ in range(n)]
dxy = [(0, 1), (1, 0), (0,-1), (-1, 0)]

for i in range(n):
    for j in range(m):
        if board[i][j] == "2":
            visited[i][j] = True
            q = deque([(i,j)])

def bfs():
    global visited, res, q
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == "1" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    res[nx][ny] = res[x][y] + 1

bfs()
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == "1":
            print(-1, end=" ")
        else:
            print(res[i][j], end=" ")
    print()