import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cnt = dict()
for card in cards:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

for num in nums:
    if num in cnt:
        print(cnt[num], end=" ")
    else:
        print("0", end=" ")