import sys
input = sys.stdin.readline
n = int(input().rstrip())
li = list(map(int, input().rstrip().split()))

sum_arr = [0] * n
ans = li[0]
sum_arr[0] = li[0]
min_value = li[0]

for i in range(1, n):
    sum_arr[i] = sum_arr[i - 1] + li[i]

    if min_value > sum_arr[i]:
        min_value = sum_arr[i]
    else:
        ans = max(ans, sum_arr[i] - min_value, sum_arr[i], li[i])
    ans = max(ans, sum_arr[i], li[i])

print(ans)