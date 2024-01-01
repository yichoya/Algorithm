import sys, itertools
input = sys.stdin.readline

white = [[0] * 101 for _ in range(101)]
n = int(input())
cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    for a in range(x, x + 10):
        for b in range(y, y + 10):
            if white[a][b] == 0:
                white[a][b] = 1
                cnt += 1
print(cnt)