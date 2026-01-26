import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
classes = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    classes[i].sort()

heap = []
current_max = 0

for i in range(n):
    value = classes[i][0]
    heapq.heappush(heap, (value, i, 0))  # (값, 반 번호, 인덱스)
    current_max = max(current_max, value)

answer = float('inf')
while True:
    current_min, class_idx, idx = heapq.heappop(heap)
    answer = min(answer, current_max - current_min)
    if idx + 1 == m:
        break

    nxt = classes[class_idx][idx + 1]
    heapq.heappush(heap, (nxt, class_idx, idx + 1))
    current_max = max(current_max, nxt)

print(answer)
