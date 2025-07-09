import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 100001
time = [-1] * MAX
prev = [-1] * MAX

def bfs(start):
    q = deque()
    q.append(start)
    time[start] = 0

    while q:
        cur = q.popleft()

        if cur == k:
            return

        for nxt in (cur - 1, cur + 1, cur * 2):
            if 0 <= nxt < MAX and time[nxt] == -1:
                time[nxt] = time[cur] + 1
                prev[nxt] = cur
                q.append(nxt)


bfs(n)
print(time[k])

path = []
now = k
while now >= 0:
    path.append(now)
    now = prev[now]
path.reverse()
print(' '.join(map(str, path)))