import sys

board=[]
for _ in range(4):
    Ax,Ay,Bx,By = map(int, sys.stdin.readline().split())
    for i in range(Ax, Bx):
        for j in range(Ay, By):
            board.append((i,j))
print(len(set(board)))