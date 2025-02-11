import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
gugan = [(0, 0)]
graph = [[] for _ in range(n + 1)]
idx = 0

def dfs(a, b, visited):
    if a == b:
        return 1
    visited[a] = True
    for node in graph[a]:
        if not visited[node]:
            if dfs(node, b, visited):
                return 1
    return 0

for _ in range(n):
    cmd, a, b = map(int, sys.stdin.readline().split())
    
    if cmd == 1:
        idx += 1
        gugan.append((a, b))

        # 기존 구간들과 연결 여부 확인
        for node_num, (x, y) in enumerate(gugan[1:], start=1):
            if x < a < y or x < b < y:
                graph[idx].append(node_num)
            if a < x < b or a < y < b:
                graph[node_num].append(idx)
    else:
        visited = [False] * (n + 1)
        print(dfs(a, b, visited))
