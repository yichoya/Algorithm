import sys

N, M = map(int, sys.stdin.readline().split())
info = dict()
for _ in range(N):
    url, pw = sys.stdin.readline().split()
    info[url] = pw


for _ in range(M):
    data = sys.stdin.readline().rstrip()
    print(info.get(data))