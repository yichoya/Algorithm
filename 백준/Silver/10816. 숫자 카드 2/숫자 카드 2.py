import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

count = dict()
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for n in nums:
    if n in count:
        print(count[n], end=" ")
    else:
        print("0", end=" ")