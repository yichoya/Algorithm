import sys

n, m = map(int, sys.stdin.readline().split())

def comb(n, m):
    if n == m:
        return 1

    elif m == 1:
        return n

    elif (n - m) >= m:
        a = n
        b = m
        for i in range(1, m):
            a *= n - i
            b *= i
        return (int(a//b))

    else:
       return comb(n, n - m)

print(comb(n, m))