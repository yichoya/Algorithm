import sys
input = sys.stdin.readline
n, m = map(int, input().split())
select = []
def recur(x):
    if len(select) == m:
        print(*select)
        return
    for i in range(x, n + 1):
        if i not in select:
            select.append(i)
            recur(i + 1)
            select.pop()
recur(1)