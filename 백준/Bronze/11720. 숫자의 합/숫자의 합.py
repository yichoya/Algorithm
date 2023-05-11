import sys

n = int(sys.stdin.readline())
nums = sys.stdin.readline().rstrip()

res = 0
for i in nums:
    tmp = int(i)
    res += tmp

print(res)