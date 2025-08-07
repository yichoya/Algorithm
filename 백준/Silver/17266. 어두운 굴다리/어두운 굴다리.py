import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 123456789
start, end = 0, n

def is_possible(height):
    s = 0  # 굴다리 시작점
    for idx in x:
        if idx - height > s:
            return False
        s = idx + height

    return s >= n


while start <= end:
    path = [False] * n
    mid = (start + end) // 2
    if is_possible(mid):
        ans = min(ans, mid)
        end = mid - 1
    else:
        start = mid + 1

print(ans)