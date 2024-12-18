import sys
alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12}
visited = [0 for _ in range(13)]
star = []
target = []
for i in range(5):
    tmp = list(sys.stdin.readline().rstrip())
    for j in range(9):
        if tmp[j] == 'x':
            target.append((i, j))
            continue
        if tmp[j] in alpha.keys():
            visited[(alpha[tmp[j]])] = 1
    star.append(tmp)

def isOk(star):
    if alpha[star[0][4]] + alpha[star[1][3]] + alpha[star[2][2]] + alpha[star[3][1]] != 26: return False
    if alpha[star[0][4]] + alpha[star[1][5]] + alpha[star[2][6]] + alpha[star[3][7]] != 26: return False
    if alpha[star[3][1]] + alpha[star[3][3]] + alpha[star[3][5]] + alpha[star[3][7]] != 26: return False
    if alpha[star[1][1]] + alpha[star[1][3]] + alpha[star[1][5]] + alpha[star[1][7]] != 26: return False
    if alpha[star[1][1]] + alpha[star[2][2]] + alpha[star[3][3]] + alpha[star[4][4]] != 26: return False
    if alpha[star[1][7]] + alpha[star[2][6]] + alpha[star[3][5]] + alpha[star[4][4]] != 26: return False
    return True

def recur(cur):
    if cur == len(target):
        # 직선 합 확인
        if isOk(star):
            for i in range(5):
                print(''.join(star[i]))
            exit(0)
        return
    x, y = target[cur]
    for a in alpha.keys():
        if visited[alpha[a]] == 0:
            visited[alpha[a]] = 1
            star[x][y] = a
            recur(cur + 1)
            visited[alpha[a]] = 0
            star[x][y] = 'x'
recur(0)