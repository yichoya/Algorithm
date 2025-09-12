import sys
sys.setrecursionlimit(10**6)

def recur(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return recur(20, 20, 20)

    if dp[a][b][c] != -1:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
    else:
        dp[a][b][c] = recur(a - 1, b, c) + recur(a - 1, b - 1, c) + recur(a - 1, b, c - 1) - recur(a - 1, b - 1, c - 1)


    return dp[a][b][c]


while 1:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == b == c == -1:
        exit()

    dp = [[[-1] * 21 for _ in range(21)] for _ in range(21)]
    ans = recur(a, b, c)
    print(f'w({a}, {b}, {c}) = {ans}')