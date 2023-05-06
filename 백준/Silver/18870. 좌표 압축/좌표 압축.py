import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

nums = sorted(set(arr))
ref = dict()
i = 0

for n in nums:
    ref[n] = i
    i += 1

for a in arr:
    val = ref[a]
    print(val, end=" ")