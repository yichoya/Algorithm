import sys

n, c = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(n)]
answer = -1

houses.sort()
first, last = 1, houses[-1] - houses[0]
while first <= last:
    mid = (first + last) // 2  # 최소 mid 이상 간격으로 공유기를 몇개 설치할 수 있는지 세기

    cnt = 1
    prev = houses[0]
    for house in houses[1:]:
        if house - prev >= mid:
            cnt += 1
            prev = house

    if cnt >= c:
       answer = mid
       first = mid + 1
    else:
        last = mid - 1
        
print(answer)