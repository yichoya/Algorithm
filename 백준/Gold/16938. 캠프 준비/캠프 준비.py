import sys
n, l, r, x = map(int, sys.stdin.readline().split())
level = list(map(int, sys.stdin.readline().split()))
level.sort()
cnt = 0
ans = []

def recur(idx):
    global cnt
    if len(ans) > n: return

    if len(ans) >= 2:
        if ans[-1] - ans[0] >= x and l <= sum(ans) <= r:
            cnt += 1

    for i in range(idx, n):
        ans.append(level[i])
        recur(i+1)
        ans.pop()

recur(0)
print(cnt)