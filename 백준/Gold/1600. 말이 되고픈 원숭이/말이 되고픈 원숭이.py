import sys
from collections import deque

k = int(sys.stdin.readline().rstrip())
w, h = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]

queue = deque()
dist = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
dxy = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (0, 1), (1, 0), (0, -1), (-1, 0)]

queue.append([0, 0, 0])
dist[0][0][0] = 0
def bfs():
    while queue:
        x, y, cnt = queue.popleft()

        if x == h - 1 and y == w - 1:
            return dist[x][y][cnt]

        if cnt < k:
            for i in range(8):
                nx, ny = x + dxy[i][0], y + dxy[i][1]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if graph[nx][ny] == 1:
                    continue
                if dist[nx][ny][cnt + 1] != -1:
                    continue
                queue.append([nx, ny, cnt + 1])
                dist[nx][ny][cnt + 1] = dist[x][y][cnt] + 1

        for i in range(8, 12):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                continue
            if dist[nx][ny][cnt] != -1:
                continue
            queue.append([nx, ny, cnt])
            dist[nx][ny][cnt] = dist[x][y][cnt] + 1

    return -1

print(bfs())