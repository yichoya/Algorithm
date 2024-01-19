import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().split()))

left_idx = 0
right_idx = N - 1
answer = float("inf")
left_answer = 0
right_answer = N - 1
while left_idx < right_idx:
    temp = arr[left_idx] + arr[right_idx]
    if abs(temp) < answer:
        left_answer = left_idx
        right_answer = right_idx
        answer = abs(temp)
    
    if temp == 0:
        break
    elif temp < 0:
        left_idx += 1
    else:
        right_idx -= 1

print(arr[left_answer], arr[right_answer])