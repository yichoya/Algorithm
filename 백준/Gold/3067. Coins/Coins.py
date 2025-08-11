import sys

t = int(sys.stdin.readline().rstrip())

INF = 123456789
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    coins = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())

    # dp[i]: i원을 만들 수 있는 방법의 수
    dp = [0] * (m + 1)
    dp[0] = 1

    # 동전 단위 고정 → 금액 증가
    for coin in coins:
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]

    print(dp[m])
