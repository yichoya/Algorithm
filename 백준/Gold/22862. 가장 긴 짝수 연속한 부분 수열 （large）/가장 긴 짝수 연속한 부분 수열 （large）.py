import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

l = 0
cnt = 0
length = 0

for r in range(n):
    if arr[r] % 2 != 0:
        cnt += 1

    while cnt > k:
        if arr[l] % 2 != 0:
            cnt -= 1
        l += 1

    length = max(length, r - l + 1 - cnt)

print(length)
