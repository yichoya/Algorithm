import sys
input = sys.stdin.readline

n = int(input())

start = 1
end = 1
cur_sum = 1
cnt = 0

while start <= n:
    if cur_sum < n:
        end += 1
        cur_sum += end
    elif cur_sum > n:
        cur_sum -= start
        start += 1
    
    # cur_sum == n
    else:
        cnt += 1
        cur_sum -= start
        start += 1

print(cnt)
