import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
ans = []
selected = [0] * n
max_res = -1

def calc(li):
    res = 0
    for i in range(n - 1):
        res += abs(li[i] - li[i + 1])
    return res

def recur():
    global max_res
    if len(ans) == n:
        res = calc(ans)
        if res > max_res:
            max_res = res
        return

    for i in range(n):
        if not selected[i]:
            selected[i] = 1
            ans.append(nums[i])
            recur()
            selected[i] = 0
            ans.pop()
recur()
print(max_res)