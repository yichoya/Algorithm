import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

#dp[i]:i번째까지 왔을때 수열의 최대 길이 - 증가할때/감소할때 
dp = [[1] * n for _ in range(2)]

for i in range(1,n):
    # 증가할 때
    if num[i - 1] <= num[i]:
        dp[0][i] = dp[0][i - 1]+1                         
    # 감소할 때
    if num[i - 1] >= num[i]:
        dp[1][i] = dp[1][i - 1]+1

print(max(map(max, dp)))