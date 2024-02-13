import sys
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
target = 0
for i in arr:
    if target + 1 < i:
        break
    target += i
print(target + 1)