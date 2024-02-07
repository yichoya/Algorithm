import sys
input = sys.stdin.readline
n, s = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
select = []

def recur(start):
    global cnt
    if sum(select) == s and len(select) > 0:
        cnt += 1
    for i in range(start, n):
        select.append(num[i])
        recur(i + 1)
        select.pop()
recur(0)
print(cnt)