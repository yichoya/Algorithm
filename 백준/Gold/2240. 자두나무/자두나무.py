import sys
t, w = map(int, sys.stdin.readline().split())
tree = [int(sys.stdin.readline()) for _ in range(t)]

def recur():
    dp = [[0] * (w + 1) for _ in range(t + 1)]
    for time in range(1, t + 1):
        for move in range(w + 1):
            cur = 1 if move % 2 == 0 else 2
            if tree[time - 1] == cur:
                if move == 0:
                    dp[time][move] = dp[time - 1][move] + 1
                else:
                    dp[time][move] = max(dp[time - 1][move], dp[time - 1][move - 1]) + 1
            else:    # 자두가 떨어지는 위치 != 내가 서있는 위치 => 자두 못받는 경우
                if move == 0:
                    dp[time][move] = dp[time - 1][move]
                else:
                    dp[time][move] = max(dp[time - 1][move], dp[time - 1][move - 1])
    return max(dp[t])

print(recur())
