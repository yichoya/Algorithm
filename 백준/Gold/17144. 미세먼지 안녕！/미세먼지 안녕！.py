import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
room, airCleaner = [], []

for i in range(r):
    room.append(list(map(int, input().split())))
    for j in range(len(room[i])):
        if room[i][j] == -1:
            airCleaner.append((i, j))


def spreadDust():
    steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    amount = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                turn = 0
                for dx, dy in steps:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in airCleaner:
                        turn += 1
                        amount[nx][ny] += room[i][j] // 5
                room[i][j] = room[i][j] - (room[i][j] // 5 * turn)
    # 남은 미세먼지 양 계산
    for i in range(r):
        for j in range(c):
            room[i][j] += amount[i][j]
    return


def runUpperCleaner():
    # 바람이 반시계 방향으로 움직임
    up_step = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    direct = 0
    x, y = airCleaner[0]
    up, y = x, 1
    previous = 0
    while True:
        nx, ny = x + up_step[direct][0], y + up_step[direct][1]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        room[x][y], previous = previous, room[x][y]
        x, y = nx, ny
    return


def runLowerCleaner():
    # 바람이 시계 방향으로 움직임
    down_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direct = 0
    x, y = airCleaner[1]
    down, y = x, 1
    previous = 0
    while True:
        nx, ny = x + down_step[direct][0], y + down_step[direct][1]
        # 처음 위치로 되돌아오면 종료
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        room[x][y], previous = previous, room[x][y]
        x, y = nx, ny
    return


for _ in range(t):
    spreadDust()
    runUpperCleaner()
    runLowerCleaner()

ans = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            ans += room[i][j]

print(ans)