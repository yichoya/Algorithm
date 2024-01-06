import sys
input = sys.stdin.readline

n = int(input())
csod = 0
for i in range(2, n):
    csod += ((n//i - 1) * i)
print(csod % 1000000)