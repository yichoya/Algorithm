import sys
import heapq

m, n = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# dp[x][y] = (x, y)까지 이동하는 동안 부순 벽의 최소 개수
dp = [[12345] * m for _ in range(n)]
dp[0][0] = 0
queue = [(0, 0, 0)]

def bfs():
    while queue:
        cost, x, y = heapq.heappop(queue)

        if x == n - 1 and y == m - 1:
            return cost

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            cur = board[nx][ny] + cost
            if cur < dp[nx][ny]:
                dp[nx][ny] = cur
                heapq.heappush(queue, (cur, nx, ny))

print(bfs())
