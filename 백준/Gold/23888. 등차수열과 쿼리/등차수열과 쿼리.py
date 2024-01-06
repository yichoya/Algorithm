import sys
input = sys.stdin.readline

def getGCD(x, y):
    if x % y == 0:
        return y
    return getGCD(y, x % y)
    
a, d = map(int, input().split())
q = int(input())
for _ in range(q):
    c, start, end = map(int, input().split())

    if c == 1:
        n = end + 1 - start
        print(int(n * (2 * a + (start + end - 2) * d) / 2)) 
    else:
        gcd = a + (start - 1) * d
        for i in range(start, end):
            cur = a + (i - 1) * d
            gcd = getGCD(gcd, cur + d)
        print(gcd)