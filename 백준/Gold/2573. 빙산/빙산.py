import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))

def count_chunks(board, n, m):
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and not visited[i][j]:
                cnt += 1
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if board[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))

    return cnt


def melt(iceberg):
    tmp_iceberg = [row[:] for row in iceberg]
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:
                cnt = 0
                for dx, dy in dxy:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if iceberg[ni][nj] == 0:
                            cnt += 1
                tmp_iceberg[i][j] = max(0, iceberg[i][j] - cnt)
    return tmp_iceberg


q = deque()
for i in range(n):
    for j in range(m):
        if iceberg[i][j] != 0:
            q.append((i, j))

year = 0
while 1:
    chunks = count_chunks(iceberg, n, m)
    if chunks == 0:
        print(0)
        break
    elif chunks >= 2:
        print(year)
        break

    iceberg = melt(iceberg)
    year += 1

