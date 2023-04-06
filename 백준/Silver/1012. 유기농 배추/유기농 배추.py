from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if farm[nx][ny] == 0:
                continue
            if farm[nx][ny] == 1:
                farm[nx][ny] = 0
                queue.append((nx, ny))

t = int(input())

for i in range(t):
# 헷갈려서 가로길이 n 세로길이 m으로 받음
    n, m, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    cnt = 0
    for j in range(k):
        x, y = map(int, input().split())
        farm[x][y] = 1

    for a in range(n):
        for b in range(m):
            if farm[a][b] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)