import sys

equation = sys.stdin.readline().rstrip().split("-")

nums = []
for i in equation:
    tmp = 0
    i = i.split("+")
    for j in i:
        tmp += int(j)
    nums.append(int(tmp))

ans = nums[0]
if len(nums) > 1:  
    for k in range(1, len(nums)):
        ans -= nums[k]

print(ans)