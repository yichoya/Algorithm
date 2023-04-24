import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque()
for i in range(1, N + 1):
    queue.append(i)

res = []
while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    res.append(queue.popleft())

print('<', end="")
print(', '.join(map(str, res)), end="")
print('>')