import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    tmp = list(sys.stdin.readline().rstrip())
    board.append(tmp)

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            redX, redY = i, j
        if board[i][j] == 'B':
            blueX, blueY = i, j

q = deque()
q.append((redX, redY, blueX, blueY, 0))
 
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[redX][redY][blueX][blueY] = 1 # 방문처리
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        redX, redY, blueX, blueY, cnt = q.popleft()
        
        if (cnt > 10):
            break 
    
        if board[redX][redY] == 'O':
            print(1)
            return
        
        for i in range(4):
            # RED
            redNX, redNY = redX, redY
            while True:
                redNX += dx[i]
                redNY += dy[i]
                # 탈출조건1 - 벽
                if board[redNX][redNY] == '#':
                    redNX -= dx[i]
                    redNY -= dy[i]
                    break
                # 탈출조건2 - 구멍
                if board[redNX][redNY] == 'O':
                    break
            
            # BLUE
            blueNX, blueNY = blueX, blueY
            while True:
                blueNX += dx[i]
                blueNY += dy[i]
                # 탈출조건1 - 벽
                if board[blueNX][blueNY] == '#':
                    blueNX -= dx[i]
                    blueNY -= dy[i]
                    break
                # 탈출조건2 - 구멍
                if board[blueNX][blueNY] == 'O':
                    break
            
            # Blue가 구멍에 들어가면 끝
            if board[blueNX][blueNY] == 'O': continue
            
            # BLUE와 RED가 같은 위치라면 더 멀리서 온 것을 뒤로 빼야한다.
            if (redNX == blueNX and redNY == blueNY):
                if( abs(redNX - redX) + abs(redNY - redY) > abs(blueNX - blueX) + abs(blueNY - blueY) ):
                    redNX -= dx[i]
                    redNY -= dy[i]
                else:
                    blueNX -= dx[i]
                    blueNY -= dy[i]
            
            if visited[redNX][redNY][blueNX][blueNY] == 0:
                q.append((redNX, redNY, blueNX, blueNY, cnt+1))
                visited[redNX][redNY][blueNX][blueNY] = 1 # 방문처리    
    print(0)
 
bfs()