import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
bag = [(0, 0)]
for _ in range(N):
    W, V = map(int, sys.stdin.readline().rstrip().split())
    bag.append((W, V))

# v값이 저장되는 이차원배열    
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = bag[i]
    for j in range(1, K + 1):
        if w > j:
            # i번째 물건 안넣음
            dp[i][j] = dp[i - 1][j]
        else:
            # max(i번째 물건 안넣고 j의 무게를 만드는 경우, i번째 물건을 넣고 j의 무게를 만드는 경우)
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])
#print(dp)