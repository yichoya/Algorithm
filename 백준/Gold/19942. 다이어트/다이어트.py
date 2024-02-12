import sys
from collections import deque

N = int(sys.stdin.readline())
mp, mf, ms, mv = map(int, sys.stdin.readline().split())
foods = [0]
for i in range(N):
    foods.append(list(map(int, input().split())))

ans = []
MAX = 1e9

def recur(p, f, s, v, price, index, visit):
    global MAX, N
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if price <= MAX:
            if price < MAX:
                ans.clear()
            MAX = price
            ans.append(visit)

    if N + 1 == index: 
        
        return

    recur(p + foods[index][0], f + foods[index][1], s + foods[index][2], v + foods[index][3],
          price + foods[index][4], index + 1, visit + [index])
    recur(p, f, s, v, price, index + 1, visit)


recur(0, 0, 0, 0, 0, 1, [])
if MAX == 1e9:
    print(-1)
else:
    print(MAX)
    print(" ".join(map(str, ans[0])))