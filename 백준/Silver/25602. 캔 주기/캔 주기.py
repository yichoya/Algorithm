import sys
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
r = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
m = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

res = -1234
def recur(depth, ans):
    global res
    if depth == k:
        res = max(ans, res)
        return
    for i in range(n):
        if a[i] == 0: continue
        a[i] -= 1
        for j in range(n):
            if a[j] == 0: continue
            a[j] -= 1

            recur(depth + 1, ans + r[depth][i] + m[depth][j])
            a[j] += 1
        a[i] += 1


recur(0, 0)
print(res)