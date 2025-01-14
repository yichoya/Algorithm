import sys

n = int(sys.stdin.readline())
board = [[0] * n for _ in range(n)]
dia1 = [0 for _ in range(2 * n - 1)]  # 우상향 대각성(/)
dia2 = [0 for _ in range(2 * n - 1)]  # 우하향 대각선(\)
col = [0 for _ in range(2 * n - 1)]
res = 0

def recur(depth):
    global res

    if depth == n:
        res += 1
        return
    # (x, y) = (depth, i)
    for i in range(n):
        if dia1[depth + i] == 0 and dia2[depth - i + (n - 1)] == 0 and col[i] == 0:
            dia1[depth + i] = dia2[depth - i + (n - 1)] = col[i] = 1
            recur(depth + 1)
            dia1[depth + i] = dia2[depth - i + (n - 1)] = col[i] = 0

recur(0)
print(res)