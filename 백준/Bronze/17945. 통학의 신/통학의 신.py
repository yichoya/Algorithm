import sys

A, B = map(int, sys.stdin.readline().split())
for x in range(-1000, 1001):
    if x * x + 2 * A * x + B == 0:
        print(x, end=' ')