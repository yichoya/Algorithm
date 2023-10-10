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

# 왜 BLUE도 방문처리를 해야되는걸가 .........
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[redX][redY][blueX][blueY] = 1
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        redX, redY, blueX, blueY, cnt = q.popleft()

        if board[redX][redY] == 'O':
            print(1)
            return

        if (cnt > 10):
            break 
        
        for i in range(4):
            # RED
            nRedX, nRedY = redX, redY
            while True:
                nRedX += dx[i]
                nRedY += dy[i]

                if board[nRedX][nRedY] == '#':
                    nRedX -= dx[i]
                    nRedY -= dy[i]
                    break

                if board[nRedX][nRedY] == 'O':
                    # print(1)
                    # return
                    break
            
            # BLUE
            nBlueX, nBlueY = blueX, blueY
            while True:
                nBlueX += dx[i]
                nBlueY += dy[i]

                if board[nBlueX][nBlueY] == '#':
                    nBlueX -= dx[i]
                    nBlueY -= dy[i]
                    break

                if board[nBlueX][nBlueY] == 'O': break

            # BLUE 탈출하면 끝
            if board[nBlueX][nBlueY] == 'O': continue
            
            # RED, BLUE 위치가 같을 때 ???
            if (nRedX == nBlueX and nRedY == nBlueY):
                if( abs(nRedX - redX) + abs(nRedY - redY) > abs(nBlueX - blueX) + abs(nBlueY - blueY) ):
                    nRedX -= dx[i]
                    nRedY -= dy[i]
                else:
                    nBlueX -= dx[i]
                    nBlueY -= dy[i]


            if visited[nRedX][nRedY][nBlueX][nBlueY] == 0:
                q.append((nRedX, nRedY, nBlueX, nBlueY, cnt+1))
                visited[nRedX][nRedY][nBlueX][nBlueY] = 1

    print(0)

bfs()