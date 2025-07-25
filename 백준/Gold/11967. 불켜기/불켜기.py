import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
rooms = [[0] * (n + 1) for _ in range(n + 1)]
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
switches = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    x, y, a, b = map(int, sys.stdin.readline().split())
    switches[x][y].append((a, b))


rooms[1][1] = 1
cnt = 1

while True:
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    q = deque()
    q.append((1, 1))
    visited[1][1] = 1

    changed = False  # 새로 불 켠 게 있는지 체크

    while q:
        x, y = q.popleft()

        # 스위치 켜기
        for a, b in switches[x][y]:
            if rooms[a][b] == 0:
                rooms[a][b] = 1
                cnt += 1
                changed = True

        for dx, dy in dxy: # 인접 칸으로 이동
            nx, ny = x + dx, y + dy
            if 0 < nx <= n and 0 < ny <= n:
                if rooms[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    # 새로 불 켠 게 없으면 종료
    if not changed:
        break

print(cnt)