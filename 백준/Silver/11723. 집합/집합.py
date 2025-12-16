import sys
input = sys.stdin.readline

m = int(input())
mask = 0

for _ in range(m):
    cmd = input().split()

    if cmd[0] == "add":
        x = int(cmd[1])
        mask |= (1 << x)

    elif cmd[0] == "remove":
        x = int(cmd[1])
        mask &= ~(1 << x)

    elif cmd[0] == "check":
        x = int(cmd[1])
        print(1 if mask & (1 << x) else 0)

    elif cmd[0] == "toggle":
        x = int(cmd[1])
        mask ^= (1 << x)

    elif cmd[0] == "all":
        mask = (1 << 21) - 1

    elif cmd[0] == "empty":
        mask = 0