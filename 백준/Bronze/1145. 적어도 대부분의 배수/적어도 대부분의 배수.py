import sys

nums = list(map(int, sys.stdin.readline().split()))
for i in range(1, 1000001):
    cnt = 0
    for n in nums:
        if i % n == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break