n = int(input())
dp = [False] * (1001) # dp[i]는 N=i일 때 상근이가 이기는지 여부
dp[1] = True
dp[3] = True
dp[4] = True

for i in range(5, n + 1):
    if dp[i - 1] and dp[i - 3] and dp[i - 4]:
        dp[i] = False
    else:
        dp[i] = True
  
if dp[n]:
    print("SK")
else:
    print("CY")