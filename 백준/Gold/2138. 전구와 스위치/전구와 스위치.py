import sys

n = int(sys.stdin.readline())
cur = list(map(int, sys.stdin.readline().rstrip()))
goal = list(map(int, sys.stdin.readline().rstrip()))

# 시작 상태(0번째 스위치를 눌렀냐, 안눌렀냐)에 따라 전체 경로가 결정됨
# flag: 시작 상태

def click(arr, idx):
    for i in [-1, 0, 1]:
        new_idx = idx + i
        if 0 <= new_idx < n:
            arr[new_idx] = 0 if arr[new_idx] == 1 else 1

def solution(flag):
    tmp = cur[:]
    cnt = 0

    if flag:
        click(tmp, 0)
        cnt += 1

    for j in range(1, n):
        if tmp[j - 1] != goal[j - 1]:
            click(tmp, j)
            cnt += 1

    return cnt if tmp == goal else 123456789

ans = min(solution(True), solution(False))
print(ans if ans != 123456789 else -1)