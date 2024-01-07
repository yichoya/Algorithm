import sys
input = sys.stdin.readline

def getGCD(x, y):
    if y == 0:
        return x
    return getGCD(y, x % y)

n = int(input())
for _ in range(n):
    li = list(map(int, input().split()))
    li.sort()
    gcd = -1
    for i in range(0, len(li) - 1):
        for j in range(i + 1, len(li)):
            gcd = max(gcd, getGCD(li[i], li[j]))
    print(gcd)