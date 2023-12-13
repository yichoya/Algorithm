import sys
n = int(sys.stdin.readline())
members = []
locX = []
locY = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    members.append((x, y))
    locX.append(x)
    locY.append(y)

locX.sort()
locY.sort()
conX = locX[(n - 1) // 2]
conY = locY[(n - 1) // 2]

sum = 0
for i in range(n):
    sum += abs(conX - members[i][0]) + abs(conY - members[i][1])
print(sum)