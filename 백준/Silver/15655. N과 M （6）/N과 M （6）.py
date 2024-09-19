import sys
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
select = []
def recur(start):
    if len(select) == m:
        print(*select)
        return
    for i in range(start, n):
        select.append(nums[i])
        recur(i + 1)
        select.pop()
recur(0)