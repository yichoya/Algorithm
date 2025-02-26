import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(li)
ans = 1234567890
while start <= end:
    mid = (start + end) // 2
    cnt = 1

    cur_max = li[0]
    cur_min = li[0]
    for i in range(len(li)):
        cur_max = max(cur_max, li[i])
        cur_min = min(cur_min, li[i])

        if cur_max - cur_min > mid:
            cnt += 1
            cur_max = li[i]
            cur_min = li[i]

    if cnt <= m:
        ans = min(ans, mid)
        end = mid - 1
    else:   # mid 값이 너무 작아 구간이 많이 생기는 경우 -> mid 증가
        start = mid + 1

print(ans)