import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
bag = []
for _ in range(N):
    W, V = map(int, sys.stdin.readline().rstrip().split())
    bag.append((W, V))

dp = [0 for _ in range(K + 1)] # 가치 체크 배열
for b in bag:
    w, v = b
    for i in range(K, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)
print(dp[-1])