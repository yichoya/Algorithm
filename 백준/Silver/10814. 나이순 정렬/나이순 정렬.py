import sys

N = int(sys.stdin.readline())

members = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    members.append((i, int(age), name))

members.sort(key= lambda x:(x[1], x[0]))

for j in members:
    print(j[1], j[2])