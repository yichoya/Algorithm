import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
for i in range(1, 1000001):
    check = 0
    for n in nums:
        if i % n == 0:
            check += 1
    if check >= 3:
        print(i)
        break