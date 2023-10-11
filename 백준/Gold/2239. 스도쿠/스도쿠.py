import sys

sudoku = []
zero = []

for i in range(9):
    tmp = list(map(int, sys.stdin.readline().rstrip()))
    sudoku.append(tmp)
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append([i, j])

def checkRowCol(x, y, num):
    for i in range(9):
        if sudoku[x][i] == num: return False
        if sudoku[i][y] == num: return False

    return True

def checkAround(x, y, num):
    nx = x // 3 * 3
    ny = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if sudoku[nx + i][ny + j] == num:
                return False
    return True

def dfs(cnt):
    if cnt == len(zero):
        for j in range(9):
            #print(*sudoku[i])
            print("".join(map(str, sudoku[j])))
        exit(0)

    # 1~9 넣으면서 확인
    for i in range(1, 10):
        x = zero[cnt][0]
        y = zero[cnt][1]

        if checkAround(x, y, i) and checkRowCol(x, y, i):
            sudoku[x][y] = i
            dfs(cnt + 1)
            sudoku[x][y] = 0

dfs(0)