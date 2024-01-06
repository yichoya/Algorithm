import sys
input = sys.stdin.readline

def getGCD(x, y):
    if y == 0:
        return x
    return getGCD(y, x % y)

a, d = map(int, input().split())
q = int(input())
for _ in range(q):
    c, start, end = map(int, input().split())

    if c == 1:
        n = end + 1 - start
        if start == end:
            print(a + (start - 1) * d)
        else:
            print(int(n * (2 * a + (start + end - 2) * d) / 2)) 
    else:
        if start == end:
            print(a + (start - 1) * d)
        else:
            print(getGCD(a, d))