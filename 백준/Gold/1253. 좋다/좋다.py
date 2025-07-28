import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 0
nums.sort()

# 투포인터로 nums[i] == nums[j] + nums[k] 성립하는 수 확인
# i != j, i != k, j < k

for i in range(n):
    target = nums[i]
    s, e = 0, n - 1

    while s < e:
        if s == i:
            s += 1
            continue
        if e == i:
            e -= 1
            continue

        total = nums[s] + nums[e]
        if target == total:
            cnt += 1
            break
        elif target < total:
            e -= 1
        else:
            s += 1

print(cnt)