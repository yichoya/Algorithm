import sys

N = int(sys.stdin.readline())
checkers = []
for _ in range(N):
    checkers.append(list(map(int, sys.stdin.readline().split())))

res = [1e9] * (N + 1)
for i in range(N):
    for j in range(N):  # 모든 교점 확인
        curX, curY = checkers[i][0], checkers[j][1]
        # 특정 위치에서 모든 체커까지의 최소 거리 계산
        dist = []
        for checker in checkers:
            dist.append(abs(curX - checker[0]) + abs(curY - checker[1]))

        dist.sort()
        total = 0
        # k개의 체커가 같은 위치(curX, curY)에 모일 때의 최소 거리 계산
        for k in range(N):
            total += dist[k]
            if res[k + 1] > total:
                res[k + 1] = total

print(*res[1:])