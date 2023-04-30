import sys
from collections import deque


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    printer = deque(list(map(int, sys.stdin.readline().split())))

    idx = deque(list(range(N)))
    cnt = 0

    while printer:
        p = printer.popleft()
        tmp = idx.popleft()
        if len(printer) == 0 or p >= max(printer):
            cnt += 1
            if tmp == M:
                print(cnt)
        else:
            printer.append(p)
            idx.append(tmp)
