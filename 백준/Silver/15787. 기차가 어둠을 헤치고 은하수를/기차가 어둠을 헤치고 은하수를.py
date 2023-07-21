import sys

N, M = map(int, sys.stdin.readline().split())
trains = [[0 for _ in range(21)] for _ in range(N + 1)]
cnt = 0
check = []

for i in range(M):
    cmd = list(map(int, sys.stdin.readline().split()))

    if cmd[0] == 1:
        if trains[cmd[1]][cmd[2]] == 0:
            trains[cmd[1]][cmd[2]] = 1
    elif cmd[0] == 2:
        if trains[cmd[1]][cmd[2]] == 1:
            trains[cmd[1]][cmd[2]] = 0
    elif cmd[0] == 3:
        for j in range(20, 1, -1):
            trains[cmd[1]][j] = trains[cmd[1]][j - 1]
        trains[cmd[1]][1] = 0
    elif cmd[0] == 4:
        for j in range(1, 20):
            trains[cmd[1]][j] = trains[cmd[1]][j + 1]
        trains[cmd[1]][20] = 0

for i in range(1, N + 1):
    if trains[i] not in check:
        check.append(trains[i])
        cnt += 1

print(cnt)