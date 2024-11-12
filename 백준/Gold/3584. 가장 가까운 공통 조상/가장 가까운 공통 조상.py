import sys
sys.setrecursionlimit(10**8)
def dfs(cur, li):
    if cur != 0 and parents[cur] == 0:
        return
    li.append(parents[cur])
    dfs(parents[cur], li)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    parents = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        parents[b] = a

    x, y = map(int, sys.stdin.readline().split())
    x_parents = [x]
    y_parents = [y]
    dfs(x, x_parents)
    dfs(y, y_parents)

    # 깊이 맞춰주기
    i, j = 0, 0
    if len(x_parents) > len(y_parents):
        i = len(x_parents) - len(y_parents)
    else:
        j = len(y_parents) - len(x_parents)

    # 같은 깊이에서 최소 공통 조상 찾기
    while x_parents[i] != y_parents[j]:
        i += 1
        j += 1
    print(x_parents[i])