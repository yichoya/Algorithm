import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    ranking = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

    ranking.sort()

    cnt = 1
    best_interview = ranking[0][1]
    for paper, interview in ranking[1:]:
        if interview < best_interview:
            cnt += 1
            best_interview = interview

    print(cnt)