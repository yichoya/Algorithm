import sys

nums = [0] * 1000001
used = [False] * 10
def no_dup(num):
    tmp = []

    while num > 0:
        d = num % 10
        if used[d]:
            for x in tmp:
                used[x] = False
            return False
        used[d] = True
        tmp.append(d)
        num //= 10

    for x in tmp:
        used[x] = False

    return True


idx, cur = 1, 1
while idx <= 1000000:
    if no_dup(cur):
        nums[idx] = cur
        idx += 1
    cur += 1

while 1:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break
    print(nums[n])

