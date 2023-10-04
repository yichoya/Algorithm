import sys

n, m = map(int,sys.stdin.readline().split())
height = [[0] * (n + 1) for _ in range(n + 1)]
        
for _ in range(m):
  short, tall = map(int,sys.stdin.readline().split())
  height[tall][short] = 1


for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if height[i][k] == 1 and height[k][j] == 1:
        height[i][j] = 1


ans = 0
for i in range(1, n + 1):
  checkCnt = 0
  for j in range(1, n + 1):
    checkCnt += (height[i][j] + height[j][i])
    
  if checkCnt == (n - 1):
    ans += 1

print(ans)