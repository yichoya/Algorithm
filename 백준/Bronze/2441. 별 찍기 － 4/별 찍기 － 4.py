import sys

n = int(sys.stdin.readline())

for i in range(n):
    if i == 0:
        print("*" * n)
    else: print(" " * (i - 1), "*" * (n - i))