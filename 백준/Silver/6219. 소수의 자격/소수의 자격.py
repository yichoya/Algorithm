import sys

primes = [False, False] + [True]*4000000
for i in range(2, 4000000):
    if primes[i]:
        for j in range(2*i, 4000000, i):
            primes[j] = False
a, b, d = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(a, b + 1):
    if primes[i]:
        if str(d) in str(i):
            cnt += 1
print(cnt)