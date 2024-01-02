import sys
input = sys.stdin.readline

def isPrime(n):
    li = [0] + [1] * n
    for i in range(2, n + 1):
        if li[i]:
            for j in range(2 * i, n + 1, i):
                li[j] = 0
    return li

primes = isPrime(1000000)
for _ in range(int(input())):
    n = int(input())
    flag = True
    for i in range(2, min(1000001, int(n ** 0.5) + 1)):
        if primes[i] and not n % i:
            flag = False
            break
    print('YES' if flag else 'NO')