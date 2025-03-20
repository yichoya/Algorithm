import sys, copy
n, m = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if room[i][j] in [1, 2, 3, 4, 5]:
            cctv.append((i, j, room[i][j]))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
ans = 123456789

# cctv가 감시할 수 있는 모든 방향
dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# 0: 빈칸 / 6: 벽 / 1~5: cctv 번호
def check(new_room, x, y, directions):
    for d in directions:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or new_room[nx][ny] == 6:
                break
            if new_room[nx][ny] == 0:
                new_room[nx][ny] = 7


def recur(cur, tmp_room):
    global ans
    if cur == len(cctv):
        cnt = sum(row.count(0) for row in tmp_room)
        ans = min(ans, cnt)
        return

    cctvX, cctvY, num = cctv[cur]
    for directions in dir[num]:
        new_room = copy.deepcopy(tmp_room)
        check(new_room, cctvX, cctvY, directions)
        recur(cur + 1, new_room)


recur(0, room)
print(ans)