import sys
from collections import deque

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [0, -1, 1, 0, -1, 1, -1, 1]
res = []

def bfs(x, y):
   global cnt, w, h, data, visited
   queue = deque()
   if data[x][y] == 0 or visited[x][y] == True:
      return
   queue.append((x, y))
   visited[x][y] = True
   cnt += 1

   while queue:
      x, y = queue.popleft()
      for i in range(8):
         nx = x + dx[i]
         ny = y + dy[i]

         if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue

         if data[nx][ny] == 1 and visited[nx][ny] == False:
            visited[nx][ny] = True
            queue.append((nx, ny))

while True:
   w, h = map(int, sys.stdin.readline().split())
   
   if w == 0 and h == 0:
      break
   
   data = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
   visited = [[False] * w for _ in range(h)]
   cnt = 0
   
   for i in range(h):
      for j in range(w):
         bfs(i, j)
   res.append(cnt)

for i in res:
   print(i)