import sys

# 입력이 두 줄이라서
n, m = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
cnt = 0
res = []

def combination(cnt, n, m):
    if cnt == m:
        print(" ".join(map(str, res)))
        return
    for i in arr:
        if i not in res:
            res.append(i)
            combination(cnt + 1, n, m)
            res.pop()

combination(cnt, n, m)