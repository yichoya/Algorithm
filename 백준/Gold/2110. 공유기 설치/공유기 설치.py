import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
houses.sort()
start = 1
end = houses[-1] - houses[0]
res = 0
while(start <= end):
    mid = int((start + end) // 2)
    router = houses[0]
    cnt = 1

    for i in range(1, N):
        if houses[i] >= router + mid:
            router = houses[i]
            cnt += 1
            
    if cnt >= C: 
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)