import sys

N , K = map(int, sys.stdin.readline().split()) 
cnt = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
res = 0
for i in range(N):
    gender , grade  = map(int, sys.stdin.readline().split())
    cnt[gender][grade - 1] += 1

for i in cnt :
    for j in i:
        if j % K == 0:
            res += j//K
        else:
            res += (j//K) + 1
print(res)
