import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * c for _ in range(r)]
res = 0

def recur(x, y, dist):
    global res

    if board[x][y] == 'T':
        return
    if x == 0 and y == c - 1:
        if dist == k:
            res += 1
        return

    for i in range(4):
        nx, ny = x + dxy[i][0], y + dxy[i][1]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or board[nx][ny] == 'T':
            continue
        if visited[nx][ny]:
            continue

        visited[nx][ny] = True
        recur(nx, ny, dist + 1)
        visited[nx][ny] = False

visited[r - 1][0] = True
recur(r - 1, 0, 1)
print(res)