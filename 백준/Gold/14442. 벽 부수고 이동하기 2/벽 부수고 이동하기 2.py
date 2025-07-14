import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, 1, 0))  # x, y, cnt, broken
    visited[0][0][0] = True

    while q:
        x, y, cnt, broken = q.popleft()
        if x == n - 1 and y == m - 1:
            return cnt

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # 빈 칸
                if board[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    q.append((nx, ny, cnt + 1, broken))
                # 벽
                elif board[nx][ny] == 1 and broken < k and not visited[nx][ny][broken + 1]:
                    visited[nx][ny][broken + 1] = True
                    q.append((nx, ny, cnt + 1, broken + 1))

    return -1

print(bfs())
