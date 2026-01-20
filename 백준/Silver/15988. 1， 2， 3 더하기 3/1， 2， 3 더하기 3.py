import sys

n = int(sys.stdin.readline().rstrip())
nums = [0, 1, 2, 4, 7]
MOD = 1_000_000_009
for _ in range(n):
    i = int(sys.stdin.readline().rstrip())
    if i >= len(nums):
        for j in range(len(nums), i + 1):
            nums.append((nums[j - 1] + nums[j - 2] + nums[j - 3]) % MOD)
    print(nums[i])