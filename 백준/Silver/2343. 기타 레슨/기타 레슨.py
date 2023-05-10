import sys
input = sys.stdin.readline

N, M= map(int,input().split())
data = list(map(int,input().split()))

start = max(data)
end = sum(data)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    size = 0
    for i in data:
        size += i
        if size > mid:
            cnt += 1
            size = i
    if size <= mid:
        cnt += 1

    if cnt <= M:
        end = mid - 1
    else:
        start = mid + 1

print(end + 1)