import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited[r][c] = True
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = r + dxy[d][0], c + dxy[d][1]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            cnt += 1
            r = nx
            c = ny
            flag = 1
            break

    if flag == 0:
        back_r, back_c = r - dxy[d][0], c - dxy[d][1]
        if 0 <= back_r < n and 0 <= back_c < m and arr[back_r][back_c] == 0:
            r, c = back_r, back_c
        else:
            print(cnt)
            break