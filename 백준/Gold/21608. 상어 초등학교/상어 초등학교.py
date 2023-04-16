import sys

n = int(sys.stdin.readline())
students = [list(map(int, sys.stdin.readline().split())) for _ in range(n ** 2)]
seat = [[0] * n for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(n ** 2):
    student = students[i][0]
    tmpFriend = -1
    tmpBlank = -1
    tmpR = 0
    tmpC = 0
    for r in range(n):
        for c in range(n):
            if seat[r][c] == 0:
                friend = 0
                blank = 0
                for j in range(4):
                    nr = r + dr[j]
                    nc = c + dc[j]
                    if 0 <= nr < n and 0 <= nc < n:
                        if seat[nr][nc] in students[i][1:]:
                            friend += 1
                        if seat[nr][nc] == 0:
                            blank += 1
                
                if tmpFriend < friend or (tmpFriend == friend and tmpBlank < blank):
                    tmpFriend = friend
                    tmpBlank = blank
                    tmpR = r
                    tmpC = c
    seat[tmpR][tmpC] = student

students.sort()
res = 0
for i in range(n):
    for j in range(n):
        score = 0
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if seat[nr][nc] in students[seat[i][j] - 1]:
                    score += 1
        if score > 0:
            res += 10 ** (score - 1)
print(res)

                