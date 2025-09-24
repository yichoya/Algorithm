import sys

n = int(sys.stdin.readline().rstrip())
pole = list(map(int, sys.stdin.readline().rstrip().split()))

def lower_bound(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


lis = [pole[0]]
for num in pole[1:]:
    if lis[-1] < num:
        lis.append(num)
    else:
        idx = lower_bound(lis, num)
        lis[idx] = num

# print(lis)
print(n - len(lis))