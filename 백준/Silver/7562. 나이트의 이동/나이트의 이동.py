from collections import deque
import sys

sys.setrecursionlimit(10**6)
dx = [2,2,1,1,-1,-1,-2,-2]
dy = [1,-1,2,-2,2,-2,1,-1]

T = int(input())

def bfs():
    deq = deque()
    deq.append([now_x,now_y])
    chesspan[now_x][now_y] = 1
    while deq:
        x,y = deq.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < L and 0 <= ny < L:
                if chesspan[nx][ny] == 0:
                    chesspan[nx][ny] = chesspan[x][y] + 1
                    deq.append([nx,ny])

for _ in range(T):
    L = int(input())

    chesspan = [[0 for _ in range(L)] for _ in range(L)]
    now_x, now_y = map(int,input().split())
    move_x, move_y = map(int,input().split())
    bfs()

    print(chesspan[move_x][move_y] - 1)