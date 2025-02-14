import sys

n = int(sys.stdin.readline())
string = list(sys.stdin.readline().rstrip())
s, e = 0, 0
check = set(string[s])
res, cnt = -12345, 1

while e < len(string) - 1:
    if len(check) > n:
        s += 1
        check = set(string[s:e + 1])
        cnt -= 1
        res = max(res, cnt)
    else:
        e += 1
        check.add(string[e])
        cnt += 1

if len(check) > n:
    res = max(res, cnt - 1)
else:
    res = max(res, cnt)
print(res)