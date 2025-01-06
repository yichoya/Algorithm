import sys

n = int(sys.stdin.readline())
players = list(map(int, sys.stdin.readline().split()))
MAX = 1000001
nums = [-1] * MAX
score = [0] * n

for idx, num in enumerate(players):
    nums[num] = idx

for i in range(MAX):
    if nums[i] > -1:
        for j in range(i*2, MAX, i):
            if nums[j] > -1:
                score[nums[i]] += 1
                score[nums[j]] -= 1

print(*score)