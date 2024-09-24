import sys
sys.setrecursionlimit(10 ** 6)

board = []
blank = []
for i in range(9):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if tmp[j] == 0:
            blank.append((i, j))
    board.append(tmp)

# 숫자 사용 여부를 기록하는 배열
row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
square_check = [[False] * 10 for _ in range(9)]

# 초기 값 설정 (미리 채워진 숫자에 대해 체크)
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            num = board[i][j]
            row_check[i][num] = True
            col_check[j][num] = True
            square_check[(i // 3) * 3 + (j // 3)][num] = True

def recur(start):
    if start == len(blank):
        for i in range(9):
            print(*board[i])
        return True

    x, y = blank[start]
    square_idx = (x // 3) * 3 + (y // 3)
    for num in range(1, 10):
        if not row_check[x][num] and not col_check[y][num] and not square_check[square_idx][num]:
            board[x][y] = num
            row_check[x][num] = col_check[y][num] = square_check[square_idx][num] = True

            # 다음 단계 재귀
            if recur(start + 1):
                return True

            board[x][y] = 0
            row_check[x][num] = col_check[y][num] = square_check[square_idx][num] = False
    return False

# 스도쿠 풀이 시작
recur(0)