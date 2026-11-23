import sys

n, m = map(int, sys.stdin.readline().split())
d = dict()

for _ in range(n):
    url, pw = sys.stdin.readline().split()
    d[url] = pw

for _ in range(m):
    target = sys.stdin.readline().rstrip()
    print(d[target])