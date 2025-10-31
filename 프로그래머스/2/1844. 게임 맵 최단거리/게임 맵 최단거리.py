from collections import deque

def bfs(maps):
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    
    q = deque([(0, 0, 1)])
    visited[0][0] = True
    
    while q:
        x, y, dist = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return dist
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True

    return -1

def solution(maps):
    global n, m, INF
    
    n = len(maps)
    m = len(maps[0])
    INF = 1234567890
    
    answer = bfs(maps)
    
    return answer