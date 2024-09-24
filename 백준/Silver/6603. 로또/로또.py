import sys

tc = []
while 1:
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp == [0]:
        break
    tc.append(tmp)

def recur(start):
    if len(select) == 6:
        print(*select)
        return

    for i in range(start, k):
        # 고르고 빼기
        select.append(group[i])
        recur(i + 1)
        select.pop()


for t in tc:
    k, group = t[0], t[1:]
    select = []
    recur(0)
    print()