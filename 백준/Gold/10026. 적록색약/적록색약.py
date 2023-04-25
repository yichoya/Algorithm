import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]

visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def colorCheck(x, y, visited):
    color = grid[x][y]
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if grid[nx][ny] == color and visited[nx][ny] == False:
                colorCheck(nx, ny, visited)

cnt1, cnt2 = 0, 0

for x in range(N):
    for y in range(N):
        if visited1[x][y] == False:
            colorCheck(x,y, visited1)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

for x in range(N):
    for y in range(N):
        if visited2[x][y] == False:     
            colorCheck(x, y, visited2)
            cnt2 += 1

print(cnt1, cnt2)