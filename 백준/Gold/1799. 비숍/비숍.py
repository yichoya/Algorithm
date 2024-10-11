# import sys
#
# n = int(sys.stdin.readline())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# # 놓을 수 있는 모든 위치 기록
# positions = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
#
# # 대각선 체크 배열
# diag1 = [0] * (2 * n)  # / 방향 대각선
# diag2 = [0] * (2 * n)  # \ 방향 대각선
#
# max_count = 0
#
#
# def recur(idx, cnt):
#     global max_count
#
#     if idx >= len(positions):
#         max_count = max(max_count, cnt)
#         return
#
#     x, y = positions[idx]
#
#     if diag1[x - y + n] == 0 and diag2[x + y] == 0:
#         # 비숍을 놓을 수 있다면 대각선 체크 후 다음 단계로
#         diag1[x - y + n] = 1
#         diag2[x + y] = 1
#         recur(idx + 1, cnt + 1)
#         diag1[x - y + n] = 0
#         diag2[x + y] = 0
#
#     # 비숍을 놓지 않고 다음으로 넘어가는 경우
#     recur(idx + 1, cnt)
#
# recur(0, 0)
# print(max_count)


import sys
n = int(sys.stdin.readline().rstrip())
board = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
res = 0
visited = [0] * (2 * n - 1)    # 우하향 대각선에 비숍이 있는지 확인하는 배열
diagUp = [[] for _ in range(2 * n - 1)]    # 우상향 대각선
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            # 우상향 대각선은 x + y가 일정
            diagUp[i + j].append((i, j))

def recur(cur, cnt):
    global res
    # 가지치기: 남은 대각선에 비숍을 다 놓아도 res 보다 적은 경우
    if res >= cnt + (2 * n - 1) - cur:
        return
    if cur == 2 * n - 1:
        res = max(res, cnt)
        return

    for x, y in diagUp[cur]:
        # 우하향 대각선은 x - y가 일정
        if visited[x - y] == 0:
            visited[x - y] = 1
            recur(cur + 1, cnt + 1)
            visited[x - y] = 0
    else: recur(cur + 1, cnt)

recur(0, 0)
print(res)