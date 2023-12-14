import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
buttons = list(map(int, sys.stdin.readline().split()))

minCnt = abs(100 - N)
# 999999인 이유: 최대 입력인 500000 (6자리)에서 나올 수 있는 가장 큰 수이기 때문에
for i in range(999999):
    num = str(i)
    for j in num:
        if int(j) in buttons:
            break

    else:
        minCnt = min(minCnt, abs(N - i) + len(num))

print(minCnt)