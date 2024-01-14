import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = [0] + list(map(int, input().split()))
part_sum = sum(temp[1:k + 1])
max_sum = part_sum
for i in range(1, n - k + 1):
    part_sum = part_sum - temp[i] + temp[i + k]
    max_sum = max(max_sum, part_sum)
print(max_sum)