import sys

string1 = [""] + list(sys.stdin.readline().rstrip())
string2 = [""] + list(sys.stdin.readline().rstrip())

dp = [[""] * len(string2) for _ in range(len(string1))]

for i in range(1, len(string1)):
    for j in range(1, len(string2)):
        if string1[i] == string2[j]:
            dp[i][j] = dp[i-1][j-1] + string1[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(dp[-1][-1])