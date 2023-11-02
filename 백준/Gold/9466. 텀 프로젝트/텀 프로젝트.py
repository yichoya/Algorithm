import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    pick = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (n + 1)
    teamMember = 0
    
    def dfs(i):
        global teamMember
        visited[i] = True
        team.append(i)
        next = pick[i]
        if not visited[next]:
            dfs(next)
        else:
            if next in team:
                teamMember += len(team[team.index(next):])

    for i in range(1, n + 1):
        if not visited[i]:
            team = []
            dfs(i)
    print(n - teamMember)