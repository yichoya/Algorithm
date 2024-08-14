import sys, itertools
input = sys.stdin.readline

dwarves = []
for i in range(9):
    dwarves.append(int(input()))
dwarves.sort()
combs = itertools.combinations(dwarves, 7)
for c in combs:
    if sum(c) == 100:
        for tmp in c:
            print(tmp)
        break