from itertools import combinations
import sys

N = int(sys.stdin.readline())
nums = []

for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        tmp = list(comb)
        tmp.sort(reverse=True)
        # print(tmp)
        nums.append(int("".join(map(str, tmp))))
# print(nums)
nums.sort()

if (N < len(nums)):
    print(nums[N])
else: print(-1)