import sys

n =  int(sys.stdin.readline())

fact = 1
cnt = 0

for i in range(1, n + 1):
    fact *= i

fact = str(fact)

for f in fact[::-1]:
    if f == '0':
        cnt += 1
    else:
        print(cnt)
        break