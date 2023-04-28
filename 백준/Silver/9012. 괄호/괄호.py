import sys

n = int(sys.stdin.readline())
res = []
for _ in range(n):
    brackets = sys.stdin.readline().split()
    cnt = 0
    for i in brackets[0]:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            break 
    if cnt == 0:
        res.append('YES')
    else: res.append('NO')

for i in res:
    print(i)