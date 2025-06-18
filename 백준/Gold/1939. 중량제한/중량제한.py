import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
max_weight = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_weight = max(max_weight, c)

start, end = map(int, sys.stdin.readline().split())

# 중량 제한 내에서 이동 가능한지 확인
def dfs(cur, limit):
    visited[cur] = 1
    if cur == end:
        return True

    for nxt, weight in graph[cur]:
        if not visited[nxt] and weight >= limit:
            if dfs(nxt, limit):
                return True

    return False


left, right = 1, max_weight
ans = 0
while left <= right:
    mid = (left + right) // 2

    visited = [0] * (n + 1)
    if dfs(start, mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)