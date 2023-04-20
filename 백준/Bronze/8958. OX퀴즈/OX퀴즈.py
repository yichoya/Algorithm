n = int(input())
quiz = [list(map(str, input())) for _ in range(n)]

for i in range(n):
    cnt = 0
    score = 0
    for j in quiz[i]:
        if j == 'O':
            cnt += 1
            score += cnt
        if j == 'X':
            cnt = 0
    print(score)