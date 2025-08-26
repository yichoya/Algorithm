import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
slice = list(map(int, sys.stdin.readline().rstrip().split()))

q = deque()
for idx, s in enumerate(slice, start=1):
    q.append((idx, s))

time = 0
ans = [0] * (n + 1)
while q:
    idx, slice = q.popleft()
    time += 1
    slice -= 1
    if slice == 0:
        ans[idx] = time
    else:
        q.append((idx, slice))

print(*ans[1:])