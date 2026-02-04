import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

arr.sort()
left = 0
right = n - 1
cnt = 0
while left < right:
    tmp = arr[left] + arr[right]
    if tmp == m:
        cnt += 1
        left += 1
        right -= 1
    elif tmp < m:
        left += 1
    else:
        right -= 1

print(cnt)