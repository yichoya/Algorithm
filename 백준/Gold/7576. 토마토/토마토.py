import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

def bfs(x, y):
    global queue
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or box[nx][ny] == -1:
                continue
            if box[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))



def solution():
    global n, m, box, visited
    # 입력
    m, n = map(int, sys.stdin.readline().split())
    # box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    box = []
    remain = 0
    for i in range(n):
        box.append(list(map(int, sys.stdin.readline().split())))
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))
            elif box[i][j] == 0:
                remain += 1
    
    visited = [[False] * m for _ in range(n)]

    # 모든 토마토 == 1 -> print(0)
    # if all(0 not in b for b in box):
    #     return print(0)
    if remain == 0:
        return print(0)
    
    # bfs 실행
    if not queue:
        return print(-1)
    x, y = queue.popleft()
    bfs(x, y)

    # 토마토가 모두 익지 못하면 print(-1)
    if any(0 in b for b in box): print(-1)
    else: print(max(map(max, box)) - 1)
    return

solution()