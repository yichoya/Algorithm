import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def raining(dir, dist):
    for x, y in clouds:
        nx = (x + dx[dir] * dist) % n
        ny = (y + dy[dir] * dist) % n
        # 구름이 도착한 칸 기록하기
        new_clouds.append((nx, ny))

        # 물 1씩 증가
        board[nx][ny] += 1

def magic():
    dia_x = [-1, 1, 1, -1]
    dia_y = [1, 1, -1, -1]

    for x, y in new_clouds:
        cnt = 0
        # 대각선 위치 확인
        for i in range(4):
            nx = x + dia_x[i]
            ny = y + dia_y[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                cnt += 1
        board[x][y] += cnt

def make_cloud():
    global clouds, new_clouds

    clouds.clear()
    for i in range(n):
        for j in range(n):
            # 물이 2 이상인 칸에 구름 생성 (구름이 도착했던 칸 제외)
            if board[i][j] >= 2 and (i, j) not in new_clouds:
                clouds.append((i, j))
                # 물의 양이 2씩 줄어듬
                board[i][j] = max(0, board[i][j] - 2)
    new_clouds.clear()


clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
new_clouds = []
for _ in range(m):
    dir, dist = map(int, sys.stdin.readline().split())
    raining(dir, dist)
    magic()
    make_cloud()


res = 0
for i in range(n):
    res += sum(board[i])
print(res)