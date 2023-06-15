import sys

N = int(sys.stdin.readline())
n = set()
for _ in range(N):
    tmp = int(sys.stdin.readline())
    n.add(tmp)

n = list(n)
n.sort()

for i in n:
    print(i)