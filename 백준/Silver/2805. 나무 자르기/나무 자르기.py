import sys

N, M  = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
res = 0

def binary(start, end):
    while (start <= end):
        total = 0
        mid = ((start + end) // 2)
        for t in trees:
            if t > mid:
                total += t - mid
        if total < M:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    return res

print(binary(start, end))