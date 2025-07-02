import sys

code = [-1] + list(map(int, sys.stdin.readline().rstrip()))
sz = len(code)


if code[1] == 0:
    print(0)
    exit(0)

dp = [0] * (sz + 1)
dp[0] = 1  # 빈 문자열
dp[1] = 1
for i in range(2, sz + 1):
    one_digit = code[i - 1]
    two_digit = code[i - 2] * 10 + code[i - 1]

    if 1 <= one_digit <= 9:
        dp[i] += dp[i - 1]
    if 10 <= two_digit <= 26:
        dp[i] += dp[i - 2]

    dp[i] %= 1000000

print(dp[sz])
