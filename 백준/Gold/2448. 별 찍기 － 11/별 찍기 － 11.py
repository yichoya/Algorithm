import sys

N = int(sys.stdin.readline())
board = [[' ' for _ in range(N * 2)] for _ in range(N)]

def triangle(x, y, N):
    if N == 3:
        board[x][y] = '*'
        board[x + 1][y - 1] = board[x + 1][y + 1] = '*'
        board[x + 2][y - 2] = board[x + 2][y - 1] = board[x + 2][y] = board[x + 2][y + 1] = board[x + 2][y + 2] = '*'
        return
    
    triangle(x, y, N // 2)
    triangle(x + (N // 2), y -  (N // 2), N // 2)
    triangle(x + (N // 2), y + (N // 2), N // 2)


x = 0
y = N 
triangle(x, y, N)

for i in range(N):
    print("".join(board[i][1:]))