import sys
from collections import deque

def checkR(n, d):
    if (n > 4 or wheel[n - 1][2] == wheel[n][6]): return
    if (wheel[n - 1][2] != wheel[n][6]):
        checkR(n + 1, -d)
        wheel[n].rotate(d)

def checkL(n, d):
    if (n < 1 or wheel[n + 1][6] == wheel[n][2]): return
    if (wheel[n + 1][6] != wheel[n][2]):
        checkL(n - 1, -d)
        wheel[n].rotate(d)


wheel = {}
for i in range(1, 5):
    wheel[i] = deque(list(map(int, sys.stdin.readline().rstrip())))
    
K = int(sys.stdin.readline())

for _ in range(K):
    n, d = map(int, sys.stdin.readline().split())

    # 기준 톱니바퀴의 오른쪽/왼쪽 톱니가 회전 가능한지를 확인하고 회전시킨다.
    checkR(n + 1, -d)
    checkL(n - 1, -d)
    wheel[n].rotate(d)

res = 0

for i in range(4):
    # 파이썬 삼항연산자: (True) if (condition) else (False)
    res += 2 ** i if wheel[i + 1][0] == 1 else 0

print(res)