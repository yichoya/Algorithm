import sys

n = int(sys.stdin.readline())

arr = [0, 1, 3, 5]

if n >= 4:
    for i in range(4, n + 1):
        arr.append(arr[i - 2] * 2 + arr[i - 1])

print(arr[n] % 10007)