import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
sushi *= 2
cnt = defaultdict(int)
ans = len(cnt)

# 윈도우 세팅
for i in range(k):
    cnt[sushi[i]] += 1
cnt[c] += 1

for l in range(n):
    cnt[sushi[l]] -= 1
    if cnt[sushi[l]] == 0:
        del cnt[sushi[l]]
    
    r = l + k
    cnt[sushi[r]] += 1
    ans = max(ans, len(cnt))

print(ans)