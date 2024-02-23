import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [1] * N  # 길이 저장
li = [[A[x]] for x in range(N)]  # 배열 저장

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + 1: 
            dp[i] = dp[j] + 1
            li[i] = li[j] + [A[i]]
m = max(dp)
print(m)
print(*li[dp.index(m)])