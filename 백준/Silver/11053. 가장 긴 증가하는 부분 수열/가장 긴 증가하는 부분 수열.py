import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# dp[i]: A[i]를 마지막 값으로 갖는 가장 긴 부분수열의 길이
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))