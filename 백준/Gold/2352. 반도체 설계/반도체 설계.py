import sys

n = int(sys.stdin.readline())
port = list(map(int, sys.stdin.readline().split()))
lis = []

# num이 들어갈 수 잇는 가장 왼쪽 인덱스 반환
def binary_search(num):
    s, e = 0, len(lis)
    while s < e:
        mid = (s + e) // 2
        if lis[mid] < num:
            s = mid + 1
        else:
            e = mid
    return e

lis.append(port[0])
for i in range(1, n):
    idx = binary_search(port[i])
    if idx == len(lis):
        lis.append(port[i])
    else:
        lis[idx] = port[i]

print(len(lis))