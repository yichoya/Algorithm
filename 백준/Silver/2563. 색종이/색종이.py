import sys

board = []
N = int(sys.stdin.readline())
for _ in range(N):
    Ax, Ay = map(int, sys.stdin.readline().split())
    Bx, By = Ax + 10, Ay + 10
    for i in range(Ax, Bx):
        for j in range(Ay, By):
            board.append((i,j))
print(len(set(board)))