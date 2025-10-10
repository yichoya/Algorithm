import sys
from collections import deque
input = sys.stdin.readline


def find_fishes(sx, sy, sz):

    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    q = deque([(sx, sy, 0)])
    fishes = []
    min_dist = 123456789

    while q:
        x, y, dist = q.popleft()

        if dist > min_dist:
            break

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] <= sz:
                    visited[nx][ny] = True
                    if 0 < board[nx][ny] < sz:
                        fishes.append((nx, ny, dist + 1))
                        min_dist = dist + 1
                    else:
                        q.append((nx, ny, dist + 1))

    fishes.sort(key=lambda x: (x[2], x[0], x[1]))
    return fishes


n = int(input().rstrip())
board = [list(map(int, input().split())) for _ in range(n)]

for x in range(n):
    for y in range(n):
        if board[x][y] == 9:
            shark_x, shark_y = x, y
            board[x][y] = 0
            break

dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
time = 0
cnt = 0
shark_sz = 2

while 1:
    fish_list = find_fishes(shark_x, shark_y, shark_sz)

    if not fish_list:
        break

    nx, ny, dist = fish_list[0]
    shark_x, shark_y = nx, ny
    time += dist
    board[nx][ny] = 0
    cnt += 1
    if cnt == shark_sz:
        shark_sz += 1
        cnt = 0

print(time)