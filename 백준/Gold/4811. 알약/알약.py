import sys

arr = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    arr[0][i] = 1

for i in range(1, 31):
    for j in range(i, 31):
        arr[i][j] += arr[i - 1][j] + arr[i][j - 1]
while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(arr[n][n])