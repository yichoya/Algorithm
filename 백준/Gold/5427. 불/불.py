import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(m)]


    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q_fire = deque()
    q_sang = deque()
    fire_time = [[-1] * n for _ in range(m)]
    sang_time = [[-1] * n for _ in range(m)]
    ans = False

    for i in range(m):
        for j in range(n):
            if board[i][j] == '*':
                q_fire.append((i, j))
                fire_time[i][j] = 0
            if board[i][j] == '@':
                q_sang.append((i, j))
                sang_time[i][j] = 0

    # 불 이동
    while q_fire:
        x, y = q_fire.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] in ['.', '@'] and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    q_fire.append((nx, ny))

    # 상근 이동
    while q_sang:
        x, y = q_sang.popleft()

        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
            print(sang_time[x][y] + 1)
            ans = True
            break

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                # if board[nx][ny] == '.' and (fire_time[nx][ny] > sang_time[x][y] + 1 or fire_time[nx][ny] == -1):
               if board[nx][ny] == '.' and sang_time[nx][ny] == -1:
                   if fire_time[nx][ny] == -1 or fire_time[nx][ny] > sang_time[x][y] + 1:
                        sang_time[nx][ny] = sang_time[x][y] + 1
                        q_sang.append((nx, ny))

    if not ans:
        print("IMPOSSIBLE")