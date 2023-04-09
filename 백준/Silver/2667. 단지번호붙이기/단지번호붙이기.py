from collections import deque

n = int(input())
gragh = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for i in range(n)]

def bfs(x, y):
    cnt = 0
    queue = deque()
   
    if gragh[x][y] == 1:
        queue.append((x, y))
        visited[x][y] = True
        cnt += 1

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if gragh[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

res = []

for i in range(n):
    for j in range(n):
        if gragh[i][j] == 1 and visited[i][j] == False:
            res.append(bfs(i, j))

print(len(res))
for i in sorted(res):
    print(i)