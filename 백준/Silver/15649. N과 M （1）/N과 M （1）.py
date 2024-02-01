import sys

n, m = map(int,sys.stdin.readline().split())
cnt = 0
res = []

def combination(cnt, n, m):
    if cnt == m:
        print(" ".join(map(str, res)))
        return
    for i in range(1, n + 1):
        if i not in res:
            res.append(i)
            combination(cnt + 1, n, m)
            res.pop()
            
combination(cnt, n, m)