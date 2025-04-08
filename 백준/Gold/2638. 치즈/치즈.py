import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 공기만 큐에 넣으면서 탐색
def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or n <= nx or ny < 0 or m <= ny or visited[nx][ny]:
                continue
            if cheese[nx][ny] >= 1:
                cheese[nx][ny] += 1
            else:
                q.append((nx, ny))
                visited[nx][ny] = True

def melt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] >= 3:
                cnt += 1
                cheese[i][j] = 0
            elif 0 < cheese[i][j] <= 2:
                cheese[i][j] = 1
    return cnt

time = 0
while True:
    bfs()
    melted_cheese = melt()
    if melted_cheese:
        time += 1
    else:
        print(time)
        break