import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
memory = list(map(int, sys.stdin.readline().rstrip().split()))
costs = list(map(int, sys.stdin.readline().rstrip().split()))

max_cost = sum(costs)
dp = [0] * (max_cost + 1)
# dp[cost] = 해당 비용으로 확보할 수 있는 최대 메모리

for i in range(n):
    for c in range(max_cost, costs[i] - 1, -1):
        dp[c] = max(dp[c], dp[c - costs[i]] + memory[i])

for c in range(max_cost + 1):
    if dp[c] >= m:
        print(c)
        break