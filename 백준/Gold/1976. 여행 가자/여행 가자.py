import sys
from collections import deque

def bfs(adj, start, visit):
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        node = q.popleft()

        for idx, item in enumerate(adj[node]):
            if item and visit[idx] == 0:
                visit[idx] = 1
                q.append(idx)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj = []
visit = [0] * N
for _ in range(N):
    adj.append(list(map(int, sys.stdin.readline().split())))
city = list(map(int, sys.stdin.readline().split()))
start = city[0] - 1

bfs(adj, start, visit)
flag = True
for c in city:
    if visit[c - 1] == 0:
        flag = False
        
if flag:
    print('YES')
else:
    print('NO')