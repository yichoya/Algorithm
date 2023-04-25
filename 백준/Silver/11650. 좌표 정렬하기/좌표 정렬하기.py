import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr.sort(key=lambda x:(x[0], x[1]))

for i, j in arr:
    print(i, j)