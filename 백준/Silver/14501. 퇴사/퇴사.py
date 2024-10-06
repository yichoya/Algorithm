import sys
def recur(cur, total):
    global ans
    if cur == n:
        ans = max(ans, total)
        return
    if cur > n:
        return

    recur(cur + li[cur][0], total + li[cur][1])
    recur(cur + 1, total)


n = int(sys.stdin.readline())
li = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
ans = 0
recur(0, 0)
print(ans)