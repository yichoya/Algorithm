import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key=lambda x: x[0])
res = 0

def recur(cur, end, total):
    global res

    if cur == n:
        res = max(res, total)
        return

    if end <= data[cur][0]:
        recur(cur + 1, data[cur][1], total + data[cur][2])
    recur(cur + 1, end, total)

recur(0, 0, 0)
print(res)