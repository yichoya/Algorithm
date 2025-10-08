import sys

n = int(sys.stdin.readline().rstrip())

side = [0, 1, 1]
for i in range(3, n + 2):
    side.append(side[i - 2] + side[i - 1])

ans = (side[n] + side[n + 1]) * 2
print(ans)