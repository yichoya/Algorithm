import sys

n, m = map(int, sys.stdin.readline().split())
s1 = set()
s2 = set()

for _ in range(n):
    s1.add(sys.stdin.readline().rstrip())

for _ in range(m):
    s2.add(sys.stdin.readline().rstrip())

res = list(s1 & s2)
res.sort()

print(len(res))
for r in res:
    print(r)