import sys
input = sys.stdin.readline()
a, b, n, w = map(int, input.split())
cnt = 0
for x in range(1, n):
    y = n - x
    if a * x + b * y == w:
        sheep = x
        goat = y
        cnt += 1
if cnt == 1:
    print(f'{sheep} {goat}')
else: print(-1)