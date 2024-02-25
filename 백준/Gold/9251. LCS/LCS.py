str1 = input()
str2 = input()
dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

def lcs(str1, str2):
    for i in range(1, len(str1) + 1):
        a = str1[i - 1]
        for j in range(1, len(str2) + 1):
            b = str2[j - 1]

            if a == b:
                # 지금까지의 최대 공통 부분수열에 1을 더함
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 이전의 최대 공통 부분수열은 계속해서 유지
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(str1)][len(str2)]

res = lcs(str1, str2)
print(res)
#print(dp)