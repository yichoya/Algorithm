nums = []
for _ in range(9):
    nums.append(int(input()))
M = max(nums)
print(M)
print(nums.index(M) + 1)