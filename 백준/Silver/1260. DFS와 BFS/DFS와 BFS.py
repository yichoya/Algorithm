from collections import deque

n, m, v = map(int, input().split())
# data = [[] * (n + 1)] 은 왜 안될까 ...... 왜 !!
data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

for i in range(len(data)):
    data[i].sort()


visited, visited2 = [False] * (n + 1), [False] * (n + 1)
res1, res2 = [v], [v]

def dfs(start):
    global res1
    visited[start] = True
    for i in data[start]:
        if visited[i] == False:
            res1.append(i)
            dfs(i)
dfs(v)
print(*res1)


def bfs(start):
    global res2
    queue = deque()
    queue.append(start)
    visited2[start] = True
    while queue:
        s = queue.popleft()
        for i in data[s]:
            if visited2[i] == False:
                visited2[i] = True
                queue.append(i)
                res2.append(i)

bfs(v)
print(*res2)