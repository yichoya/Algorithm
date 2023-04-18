import sys

n = int(sys.stdin.readline())
family = [[0] * (n + 1) for _ in range(n + 1)]
num1, num2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
for _ in range(m):
    p, c = map(int, input().split())
    family[p][c] = 1
    family[c][p] = 1

visited = [False] * (n + 1)
res = []

def dfs(x, depth):
    visited[x] = True
    depth += 1

    if x == num2:
        res.append(depth)
        return
    
    for i in range(1, n + 1):
        if not visited[i] and family[x][i] == 1:
            dfs(i, depth)

dfs(num1, 0)
if not res: print(-1)
else: print(res[0] - 1)