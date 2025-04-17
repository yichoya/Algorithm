import sys

n = int(sys.stdin.readline())
egg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = 0

def recur(cur, cnt):
    global res

    if cur == n:
        res = max(res, cnt)
        return

    if egg[cur][0] <= 0:
        recur(cur + 1, cnt)
        return

    can_hit = False  # 한 번이라도 쳤는지 여부
    for i in range(n):
        if i == cur or egg[i][0] <= 0: continue
        can_hit = True

        egg[i][0] -= egg[cur][1]
        egg[cur][0] -= egg[i][1]

        tmp = 0
        if egg[cur][0] <= 0:
            tmp += 1
        if egg[i][0] <= 0:
            tmp += 1

        recur(cur + 1, cnt + tmp)

        egg[i][0] += egg[cur][1]
        egg[cur][0] += egg[i][1]

    if not can_hit:
        recur(cur + 1, cnt)

recur(0, 0)
print(res)
