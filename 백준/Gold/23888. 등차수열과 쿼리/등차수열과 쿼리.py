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
        sum1 = (end * ((2 * a) + (end - 1) * d) // 2)
        sum2 = ((start - 1) * ((2 * a) + (start - 2) * d) // 2)
        print(sum1 - sum2)

    else:
        if start == end:
            print(a + (start - 1) * d)
        else:
            print(getGCD(a, d))