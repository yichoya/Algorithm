import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
select = []
def recur():
    if len(select) == m:
        print(*select)
        return
    for i in arr:
        select.append(i)
        recur()
        select.pop()
recur()