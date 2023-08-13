import sys

H, W = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))

water = 0

for i in range(1, W-1):
    maxL = max(blocks[:i]) 
    maxR = max(blocks[i+1:]) 
    
    standard = min(maxL, maxR)
    
    if blocks[i] < standard:
        water += standard - blocks[i]

print(water)

#3 6
#5 4 1 3 1 2
#ans = 3