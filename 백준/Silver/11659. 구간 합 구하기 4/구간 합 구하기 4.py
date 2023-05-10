import sys

N, M= map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

sum_data = [0, data[0]]
for d in range(1, len(data)):
    tmp = sum_data[d] + data[d]
    sum_data.append(tmp)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())

    ans = sum_data[y] - sum_data[x - 1]
    print(ans)