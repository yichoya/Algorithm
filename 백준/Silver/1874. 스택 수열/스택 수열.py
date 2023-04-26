import sys

n = int(sys.stdin.readline())

cnt = 1
tmp = True
stack = []
sign = []

for i in range(n):
    num = int(sys.stdin.readline())
    
    while cnt <= num:
        stack.append(cnt)
        sign.append('+')
        cnt += 1

    
    if stack[-1] == num:
        stack.pop()
        sign.append('-')
    
    else:
        tmp = False
        break

if tmp == False:
    print("NO")
else:
    for i in sign:
        print(i)