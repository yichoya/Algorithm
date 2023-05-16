import sys, math

N, M = map(int, sys.stdin.readline().split())

print(M - math.gcd(N, M))