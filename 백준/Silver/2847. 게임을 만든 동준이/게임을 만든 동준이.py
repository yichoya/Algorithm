import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        target = scores[i + 1] - 1
        cnt += scores[i] - target
        scores[i] = target

print(cnt)