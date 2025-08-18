import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
li = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + li[i]

cnt_max = -12345
cnt_term = 0
for j in range(x, n + 1):
    tmp = prefix[j] - prefix[j - x]
    if tmp > cnt_max:
        cnt_max = tmp
        cnt_term = 1
    elif tmp == cnt_max:
        cnt_term += 1

if cnt_max == 0:
    print("SAD")
else:
    print(cnt_max)
    print(cnt_term)
