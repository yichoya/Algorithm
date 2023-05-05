import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cards.sort()

for i in arr:
    start = 0
    end = N - 1
    check = False

    while(start <= end):
        mid = int((start + end) // 2)
        if cards[mid] > i:
            end = mid - 1
        elif cards[mid] < i:
            start = mid + 1
        else:
            check = True
            break
    print(1 if check else 0, end=' ')