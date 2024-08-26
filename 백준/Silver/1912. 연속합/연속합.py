import sys
n = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))

ans = -1e9
prefix_sum = [0] * (n + 1)
min_prefix_sum = 0

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    ans = max(ans, prefix_sum[i] - min_prefix_sum)
    min_prefix_sum = min(min_prefix_sum, prefix_sum[i])

print(ans)