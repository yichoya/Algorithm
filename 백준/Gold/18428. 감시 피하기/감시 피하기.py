from sys import stdin
from itertools import combinations
import copy
from collections import deque

N = int(input())
board = [list(map(str, stdin.readline().split())) for _ in range(N)]

teachers = deque([])
blanks = []
for i in range(N):
    for j in range(N):
        if board[i][j] == "T":
            teachers.append((i, j))
        if board[i][j] == "X":
            blanks.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(B, T):
    while T:
        x, y = T.popleft()
        for i in range(4):
            for j in range(1, N):
                nx = x + dx[i] * j
                ny = y + dy[i] * j

                if 0 <= nx < N and 0 <= ny < N:
                    if B[nx][ny] == "S":
                        return False
                    if B[nx][ny] == "O":
                        break
                else: continue
    return True


for combs in combinations(blanks, 3):
    tmp_board = copy.deepcopy(board)
    tmp_teachers = copy.deepcopy(teachers)
    for c in combs:
        tmp_board[c[0]][c[1]] = "O"
    if check(tmp_board, tmp_teachers):
        print("YES")
        break
else: print("NO")
