import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

l, r = 0, n - 1
score, max_score = 0, 0

while l < r:
    score = (r - l - 1) * min(li[l], li[r])
    max_score = max(max_score, score)

    if li[l] < li[r]:
        l += 1
    else:
        r -= 1

print(max_score)

