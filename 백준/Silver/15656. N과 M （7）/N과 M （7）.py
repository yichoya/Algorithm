import sys
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
select = []
def recur():
    if len(select) == m:
        print(*select)
        return
    for i in range(n):
        select.append(nums[i])
        recur()
        select.pop()
recur()