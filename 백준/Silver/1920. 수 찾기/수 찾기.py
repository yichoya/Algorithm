import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

arr.sort()

for n in nums:
    start = 0
    end = N - 1
    exist = False
    while(start <= end):
        mid = int((start + end) // 2)
        if arr[mid] > n:
            end = mid - 1
        elif arr[mid] < n:
            start = mid + 1
        elif arr[mid] == n:
            exist = True
            break
    if exist == True:
        print("1")
    else:
        print("0")