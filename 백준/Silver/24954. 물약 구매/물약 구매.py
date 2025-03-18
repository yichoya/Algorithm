import sys

n = int(sys.stdin.readline())
cost = list(map(int, sys.stdin.readline().split()))
li = [[] for _ in range(n)]
for i in range(n):
    num = int(sys.stdin.readline())
    if num > 0:
        for _ in range(num):
            idx, disc = map(int, sys.stdin.readline().split())
            li[i].append((idx - 1, disc))

ans = 1234567890
selected = [-1] * n  # 구매 순서 저장
visited = [False] * n

def calc():
    global selected
    total = 0
    discounted = cost[:]

    for i in selected:
        total += max(1, discounted[i])

        for idx, discount in li[i]:
            discounted[idx] -= discount

    return total


def recur(cur):
    global ans

    if cur == n:
        ans = min(ans, calc())
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            selected[cur] = i
            recur(cur + 1)
            visited[i] = False

recur(0)
print(ans)