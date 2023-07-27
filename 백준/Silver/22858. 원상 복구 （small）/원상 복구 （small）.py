import sys

N, K = map(int, sys.stdin.readline().split())

sList = list(map(int, sys.stdin.readline().split()))
dList = list(map(int, sys.stdin.readline().split()))

prev = sList

for i in range(K):
    #[0, 1, 2, 3, ..., N]
    tmp = list(range(N))
    for j in range(N):
        idx = dList[j]
        tmp[idx - 1] = prev[j]
    prev = tmp

print(*prev)