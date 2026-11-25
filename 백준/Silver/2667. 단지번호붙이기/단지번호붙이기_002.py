import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[False] * (n + 1) for _ in range(n + 1)]
ans = []

def bfs(a, b):
    q = deque([(a, b)])
    visited[a][b] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    ans.append(cnt)

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(len(ans))
ans.sort()
for a in ans:
    print(a)