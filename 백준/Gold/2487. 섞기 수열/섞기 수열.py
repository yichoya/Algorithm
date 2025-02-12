import sys
from math import lcm
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
cmd = [0] + list(map(int, sys.stdin.readline().split()))
visited = [0 for _ in range(n + 1)]
res = []

def recur(idx):
    cnt = 0
    while not visited[idx]:
        visited[idx] = 1
        idx = cmd[idx]
        cnt += 1
    return cnt

for i in range(1, n + 1):
    if not visited[i]:
        cycle_length = recur(i)
        res.append(cycle_length)

# print(res)
print(lcm(*res))
