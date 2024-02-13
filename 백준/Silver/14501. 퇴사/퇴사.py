N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def dfs(day, tmp):
    global ans
    if day == N:
        if ans < tmp:
            ans = tmp
        return
    dfs(day+1, tmp)
    if day + a[day][0] <= N:
        dfs(day+a[day][0], tmp + a[day][1])

dfs(0, 0)
print(ans)