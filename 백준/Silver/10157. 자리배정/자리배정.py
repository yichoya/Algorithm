import sys

C, R = map(int, sys.stdin.readline().split())
number = int(sys.stdin.readline())

board = [[0] * (C + 1) for _ in range(R + 1)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = 0, 0
direction = 0

if number > C * R:
    print(0)
    exit()

for seat in range(1, C * R + 1):
    if seat == number:
        print(y + 1, x + 1)
        break
    board[x][y] = seat
    x += dx[direction]
    y += dy[direction]

    if x < 0 or y < 0 or x >= R or y >= C or board[x][y]:
        x -= dx[direction]
        y -= dy[direction]
        direction = (direction + 1) % 4
        x += dx[direction]
        y += dy[direction]