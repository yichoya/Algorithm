import sys
INF = 1e9

# N, H = map(int, sys.stdin.readline().split())
# cave = [INF] + [0] * (H)
# for i in range(1, N + 1):
#     tmp = int(sys.stdin.readline().rstrip())
#     if i % 2 == 0:
#         for j in range(H, H - tmp, -1):
#             cave[j] += 1
#     else:
#         for j in range(1, tmp + 1):
#             cave[j] += 1

# obstacle = min(cave)
# cnt = cave.count(obstacle)
# print(obstacle, cnt)

N, H = map(int, sys.stdin.readline().split())
top = [0] * (H + 1) # 종유석
bottom = [0] * (H + 1) # 석순
total = [INF] + [0] * H

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if i % 2:
        top[num] += 1
    else:
        bottom[H - num + 1] += 1

# 종유석은 높이 H부터 하나씩 줄여가면서 갯수를 세준다.
# ex ) 높이가 3일때 길이가 3 이상인 종유석은 반드시 지나가게 되므로 높이를 줄여가면서 누적합(prefix sum)으로 해결할 수 있다.
for i in range(H - 1, 0, -1):
    top[i] += top[i + 1]
# 석순은 높이 1부터 하나씩 늘려가면서 갯수를 세준다.
# ex ) 높이가 3일때 길이가 3 이상인 석순은 반드시 지나가게 되므로 높이를 늘려가면서 누적합(prefix sum)으로 해결할 수 있다.
for i in range(1, H + 1):
    bottom[i] += bottom[i - 1]
# 각각의 높이에서 석순과 종유석의 누적합 더해주기
for i in range(1, H + 1):
    total[i] = top[i] + bottom[i]

ans = min(total)
print(ans, total.count(ans)) # 결과 출력
