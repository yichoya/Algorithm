import sys

N = int(sys.stdin.readline())
calendar = [0] * 366
w, h = 0, 0
ans = 0

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())

    while (start <= end):
        calendar[start] += 1
        start += 1

for i in range(1, 366):
    if calendar[i] == 0:
        ans += (w * h)
        w, h = 0, 0
        continue
    
    w += 1
    h = max(h, calendar[i])

ans += (w * h)
print(ans)