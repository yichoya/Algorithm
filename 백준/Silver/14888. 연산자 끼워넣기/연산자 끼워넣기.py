# 음수 나눗셈 주의 !!
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ops = list(map(int, sys.stdin.readline().split()))
maxVal, minVal = -1234567890, 1234567890

def recur(cur, tmp):
    global ops, maxVal, minVal

    if cur == n - 1:
        maxVal = max(maxVal, tmp)
        minVal = min(minVal, tmp)
        return

    if ops[0] >= 1:
        ops[0] -= 1
        recur(cur + 1, tmp + nums[cur + 1])
        ops[0] += 1

    if ops[1] >= 1:
        ops[1] -= 1
        recur(cur + 1, tmp - nums[cur + 1])
        ops[1] += 1

    if ops[2] >= 1:
        ops[2] -= 1
        recur(cur + 1, tmp * nums[cur + 1])
        ops[2] += 1

    if ops[3] >= 1:
        ops[3] -= 1
        recur(cur + 1, int(tmp / nums[cur + 1]))
        ops[3] += 1

recur(0, nums[0])
print(maxVal)
print(minVal)