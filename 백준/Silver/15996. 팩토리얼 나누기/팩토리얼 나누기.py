import sys
input = sys.stdin.readline

n, a = map(int, input().split())
cnt = 0
tmp = a
while tmp <= n:
    cnt += (n//tmp)
    tmp *= a

print(cnt)