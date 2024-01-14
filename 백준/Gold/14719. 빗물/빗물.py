import sys

H, W = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(1, W - 1):
    maxL = max(blocks[ : i]) 
    maxR = max(blocks[i + 1 : ]) 
    
    standard = min(maxL, maxR)
    if blocks[i] < standard:
        ans += standard - blocks[i]
print(ans)