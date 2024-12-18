import sys
a, b = map(int, sys.stdin.readline().split())
a_num = [int(num) for num in str(a)]
a_num.sort()
visited = [0 for _ in range(len(a_num))]
ans = []
tmp = -1
def recur(cur, ans):
    global tmp, visited

    if len(ans) > 1 and ans[0] == 0:
        return
    if cur == len(a_num):
        c = int(''.join(map(str, ans)))
        if b > c:
            tmp = max(tmp, c)
        else:
            print(tmp)
            exit(0)
        return

    for i in range(len(a_num)):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(a_num[i])
            recur(cur + 1, ans)
            ans.pop()
            visited[i] = 0

recur(0, [])
print(tmp)