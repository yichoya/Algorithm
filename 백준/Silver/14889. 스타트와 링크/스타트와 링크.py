import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

players = list(range(N))
answer = float('inf')

# 0번 선수 -> 스타트 팀에 고정
for comb in combinations(range(1, N), N // 2 - 1):
    start = [0] + list(comb)
    link = [p for p in players if p not in start]

    start_score = 0
    link_score = 0

    for i in range(len(start)):
        for j in range(i + 1, len(start)):
            a, b = start[i], start[j]
            start_score += S[a][b] + S[b][a]

    for i in range(len(link)):
        for j in range(i + 1, len(link)):
            a, b = link[i], link[j]
            link_score += S[a][b] + S[b][a]

    answer = min(answer, abs(start_score - link_score))

print(answer)
