import sys
from collections import defaultdict
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

li = [0] * (n + 1)

for i in range(1, n + 1):
    li[i] = li[i - 1] + a[i - 1] - b[i - 1]

count_map = defaultdict(int)
count_map[0] = 1
ans = 0
for i in range(1, n + 1):
    ans += count_map[li[i]]
    count_map[li[i]] += 1

print(ans)