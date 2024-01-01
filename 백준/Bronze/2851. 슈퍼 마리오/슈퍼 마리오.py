import sys, itertools
input = sys.stdin.readline

mushrooms = []
for _ in range(10):
    mushrooms.append(int(input().rstrip()))

score = 0
minScore = 101
maxScore = -101
for m in mushrooms:
    score += m
    if score <= 100:
        minScore = score
    if score > 100:
        maxScore = score
        break
        
if abs(100 - minScore) < abs(100 - maxScore):
    print(minScore)
else: print(maxScore)