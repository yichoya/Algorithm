import sys

R, C = map(int, sys.stdin.readline().split())
board = []
for _ in range(R):
    tmp = list(sys.stdin.readline().rstrip())
    board.append(tmp)

visited = set()
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
ans = 0

def dfs(x, y, cnt):
    global ans

    visited.add(board[x][y])
    ans = max(cnt, ans)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx >= 0 and nx < R and ny >= 0 and ny < C:
            if board[nx][ny] not in visited:
                dfs(nx, ny, cnt + 1)
                
    visited.remove(board[x][y])

dfs(0, 0, 1)
print(ans)