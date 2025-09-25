import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
scores = list(map(int, sys.stdin.readline().rstrip().split()))

l, r = 0, sum(scores)
ans = 0
while l <= r:
    mid = (l + r) // 2

    tmp = 0
    cnt = 0
    for s in scores:
        tmp += s
        if tmp >= mid:
            cnt += 1
            tmp = 0

    if cnt >= k:
        ans = max(ans, mid)
        l = mid + 1
    elif cnt < k:
        r = mid - 1

print(ans)