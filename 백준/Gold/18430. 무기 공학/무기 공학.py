import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

boomerangs = [
    [(0, 0), (0, -1), (1, 0)],
    [(0, 0), (-1, 0), (0, -1)],
    [(0, 0), (-1, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 0)]
]
visited = [[False] * m for _ in range(n)]
max_score = -12345


def recur(x, y, score):
    global max_score

    if x == n:
        max_score = max(max_score, score)
        return

    next_x, next_y = (x, y + 1) if y + 1 < m else (x + 1, 0)

    if not visited[x][y]:
        for b in boomerangs:
            flag = True
            tmp_score = 0

            for i, (dx, dy) in enumerate(b):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    pass
                else:
                    flag = False
                    break

            if flag:
                tmp_score = 0
                for i, (dx, dy) in enumerate(b):
                    nx, ny = x + dx, y + dy
                    visited[nx][ny] = True
                    if i == 0:
                        tmp_score += board[nx][ny] * 2
                    else:
                        tmp_score += board[nx][ny]

                recur(next_x, next_y, score + tmp_score)

                for i, (dx, dy) in enumerate(b):
                    nx, ny = x + dx, y + dy
                    visited[nx][ny] = False

    recur(next_x, next_y, score)

recur(0, 0, 0)
print(max_score)