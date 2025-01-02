import sys
from collections import deque

def dfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if abs(x - fest_x) + abs(y - fest_y) <= 1000:
            print('happy')
            return

        for i in range(n):
            if not visited[i]:
                tmp_x, tmp_y = cvs[i][0], cvs[i][1]
                if abs(x - tmp_x) + abs(y - tmp_y) <= 1000:
                    visited[i] = True
                    q.append(cvs[i])
    print('sad')
    return


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    home_x, home_y = map(int, sys.stdin.readline().split())
    cvs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    fest_x, fest_y = map(int, sys.stdin.readline().split())

    visited = [0 for _ in range(n + 1)]
    dfs(home_x, home_y)