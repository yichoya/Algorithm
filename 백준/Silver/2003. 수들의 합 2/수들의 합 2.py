import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
res, cnt = nums[start], 0
while(end < n):
    if res < m:
        end += 1
        if end >= n:
            break
        res += nums[end]
    elif res > m:
        res -= nums[start]
        start += 1
    else:
        cnt += 1
        res -= nums[start]
        start += 1

print(cnt)