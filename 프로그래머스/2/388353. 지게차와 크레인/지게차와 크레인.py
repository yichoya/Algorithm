from collections import deque
import copy

# (i, j) 위치의 상자가 외부와 연결가능한지 확인
def isLift(i, j, board):
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    q = deque([(i, j)])
    
    for dx, dy in dxy:
        nx, ny = i + dx, j + dy
        
        # 가장 자리
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == " ":
            q.append((nx, ny))
            visited[nx][ny] = True
    
    while q:
        x, y = q.popleft()

        # 외부에 닿으면 True
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            return True

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == " ":
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return False
    

def solution(storage, requests):
    global n, m
    answer = 0
    n = len(storage)
    m = len(storage[0])
    board = [list(row) for row in storage]

    for r in requests:
        copy_board = copy.deepcopy(board)
        for i in range(n):
            for j in range(m):
                if board[i][j] == r[0]:
                    if len(r) == 2 or isLift(i, j, copy_board):
                        board[i][j] = " "
                        
    for x in range(n):
        for y in range(m):
            if board[x][y] != " ":
                answer += 1

    return answer
