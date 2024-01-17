import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 0, 0
cnt = 0
tmp = nums[start]
while 1:
    if tmp < m:
        end += 1
        if end >= n:
            break
        tmp += nums[end]
    elif tmp > m:
        tmp -= nums[start]
        start += 1
    else:
        cnt += 1
        tmp -= nums[start]
        start += 1
print(cnt)