import sys
N = int(sys.stdin.readline())

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
board = [[0] * 101 for _ in range(101)]

for _ in range(N):
    # x:행, y:열로 바꿔서 변수 저장 -> dir 좌표도 바꿈
    y, x, d, g = map(int, sys.stdin.readline().split())
    board[x][y] = 1
    curve = [d] # 이전 세대 방향 기록
    tmp = [d]  # 이전 세대가 회전된 방향을 기록

    for _ in range(g + 1):
        for t in tmp:
            x += dir[t][0]
            y += dir[t][1]
            board[x][y] = 1
        
        tmp = [(c + 1) % 4 for c in curve]
        tmp.reverse()
        curve += tmp

# 사각형 탐색
ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            ans += 1
print(ans)