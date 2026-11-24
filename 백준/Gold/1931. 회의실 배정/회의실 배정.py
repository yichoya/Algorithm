import sys

input = sys.stdin.readline

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for start, end in times:
  if start >= end_time:
    cnt += 1
    end_time = end

print(cnt)