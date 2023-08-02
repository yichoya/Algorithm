import sys
from collections import deque

N = int(sys.stdin.readline())
balloons = deque(enumerate(map(int, sys.stdin.readline().split())))
ans = []

while balloons:
    idx, next = balloons.popleft()
    ans.append(idx + 1)

    if next > 0:
        balloons.rotate(-(next - 1))
    elif next < 0:
        balloons.rotate(-next)

#print(' '.join(map(str, ans)))
print(*ans)