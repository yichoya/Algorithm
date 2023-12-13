import sys
N = int(sys.stdin.readline())
houses = list(map(int, sys.stdin.readline().split()))
houses.sort()

# if N % 2 == 0:
#     antenna = min((houses[(N - 1) // 2], houses[N // 2]))
# else:
#     antenna = houses[(N - 1) // 2]

# print(antenna)
print(houses[(N - 1) // 2])