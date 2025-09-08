import sys, heapq

n, k = map(int, sys.stdin.readline().rstrip().split())
jewels = list(tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
bags = list(int(sys.stdin.readline().rstrip()) for _ in range(k))

jewels.sort(key=lambda x: x[0])
bags.sort()

max_heap = []
answer = 0
idx = 0

for limit in bags:
    # 현재 가방에 들어갈 수 있는 모든 보석 후보 넣기
    while idx < n and jewels[idx][0] <= limit:
        heapq.heappush(max_heap, -jewels[idx][1])  # 음수로 저장해서 최대힙처럼
        idx += 1

    if max_heap:
        answer += -heapq.heappop(max_heap)

print(answer)