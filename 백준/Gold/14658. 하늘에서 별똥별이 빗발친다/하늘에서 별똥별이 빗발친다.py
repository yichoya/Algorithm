import sys

n, m, l, k = map(int, sys.stdin.readline().split())
stars = [list(map(int, sys.stdin.readline().split()))for _ in range(k)]
# 별 두개의 좌표로 트램펄린 만들기 -> K개의 점이 트램펄린 내에 존재하는지 확인
ans = 1e9
for i in range(k):
    for j in range(k):
        x, y = stars[i][0], stars[j][1]
        cnt = 0
        for star in stars:
            starX, starY = star[0], star[1]

            if x <= starX <= x + l and y <= starY <= y + l:    # 트램펄린 범위 내에 있는지
                cnt += 1
        ans = min(ans, k - cnt)
print(ans)