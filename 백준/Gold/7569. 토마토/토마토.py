import sys
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
queue = deque()

def bfs(queue):
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                queue.append((nx, ny, nz))



def solution():
    global n, m, h, box, visited, queue
    # 입력
    m, n, h = map(int, sys.stdin.readline().split())
    box = []
    remain = 0
    for i in range(h):
        tmp = []
        for j in range(n):
            tmp.append(list(map(int, sys.stdin.readline().split())))
            for k in range(m):
                if tmp[j][k] == 1:
                    queue.append((i, j, k))
                elif tmp[j][k] == 0:
                    remain += 1
        box.append(tmp)

    if remain == 0:
        return print(0)
    
    # bfs 실행
    if not queue:
        return print(-1)
    bfs(queue)

    day = 0
    for i in box:
        for j in i:
            for k in j:
                if k == 0:
                    return print(-1)       
            day = max(day, max(j))
    return print(day - 1)

solution()