import sys

n = int(sys.stdin.readline())
line = [int(sys.stdin.readline()) for _ in range(n)]
# dp[i]: i번째에서 만들 수 있는 최장 증가 부분 수열의 길이
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))