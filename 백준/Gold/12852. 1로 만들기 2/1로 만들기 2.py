import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
# prev[i]: i로 오기 직전의 수
prev = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    prev[i] = i - 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

print(dp[n])

path = []
cur = n
while cur != 0:
    path.append(cur)
    cur = prev[cur]
print(*path)