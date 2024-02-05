import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
select = []
def recur(start) :
    if len(select) == m:
        print(*select)
        return
    for i in range(start, n):
        select.append(arr[i])
        recur(i)
        select.pop()
recur(0)