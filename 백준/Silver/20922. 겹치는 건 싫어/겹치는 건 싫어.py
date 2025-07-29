import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

count = defaultdict(int)
start = 0
ans = 0

for end in range(n):
    count[A[end]] += 1

    while count[A[end]] > k:
        count[A[start]] -= 1
        start += 1

    ans = max(ans, end - start + 1)

print(ans)
