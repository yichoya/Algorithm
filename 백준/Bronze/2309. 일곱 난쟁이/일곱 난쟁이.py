import sys
from itertools import combinations

dwarves = []
for _ in range(9):
    d =  int(sys.stdin.readline())
    dwarves.append(d)

check = list(combinations(dwarves, 7))
for c in check:
    if sum(c) == 100:
        c = list(c)
        c.sort()
        for i in c:
            print(i)
        break