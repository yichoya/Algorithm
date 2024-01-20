import sys
input = sys.stdin.readline

n, k, b = map(int,input().split())
lights = [i for i in range(0, n + 1)]
for _ in range(b):
    lights[int(input())] = -1

res = 0
for i in range(1, k + 1):
    if lights[i] == -1:
        res += 1
cnt = res
for i in range(2, n - k + 2):
    if lights[i - 1] == -1:
        cnt -= 1
    if lights[i + k - 1] == -1:
        cnt += 1
    res = min(res, cnt)
print(res)