N = int(input())

A = list(map(int, input().split()))
maxNum = max(A)
minNum = min(A)

print(maxNum * minNum)