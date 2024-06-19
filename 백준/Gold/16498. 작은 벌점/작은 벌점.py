import sys
x, y, z = map(int, sys.stdin.readline().split())
A = sorted(list(map(int, sys.stdin.readline().split())))
B = sorted(list(map(int, sys.stdin.readline().split())))
C = sorted(list(map(int, sys.stdin.readline().split())))

i, j, k = 0, 0, 0
ans = 1e9

while i < x and j < y and k < z:
    a, b, c = A[i], B[j], C[k]
    cur_max = max(a, b, c)
    cur_min = min(a, b, c)
    ans = min(ans, abs(cur_max - cur_min))

    if cur_min == a:
        i += 1
    elif cur_min == b:
        j += 1
    else:
        k += 1

print(ans)