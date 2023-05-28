n = int(input())

for j in range(1, n):
    print(" " * (n - j) + "*" * (2 * j - 1))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))