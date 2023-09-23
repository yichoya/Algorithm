import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dice = [0 for _ in range(7)]
cmd = list(map(int, sys.stdin.readline().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(c):
    if c == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif c == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif c == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif c == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

for i in cmd:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]
    
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    x, y = nx, ny
    move(i)

    if grid[x][y]:
        dice[1] = grid[x][y]
        grid[x][y] = 0
    else:
        grid[x][y] = dice[1]

    print(dice[6])