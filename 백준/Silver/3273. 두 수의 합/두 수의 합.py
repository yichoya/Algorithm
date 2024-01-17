import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
x = int(input())
number.sort()
start, end = 0, n - 1
cnt, tmp = 0, 0
while start < end:
    tmp = number[start] + number[end]
    if tmp < x:
        start += 1
    elif tmp > x:
        end -= 1
    else:
        cnt += 1
        start += 1
        end -= 1
print(cnt)