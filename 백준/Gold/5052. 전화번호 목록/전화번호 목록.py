import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    nums = []

    for _ in range(n):
        nums.append(sys.stdin.readline().rstrip())

    nums.sort()
    flag = True
    for i in range(n - 1):
        if nums[i] == nums[i + 1][:len(nums[i])]:
            flag = False
            break
    print("YES" if flag else "NO")