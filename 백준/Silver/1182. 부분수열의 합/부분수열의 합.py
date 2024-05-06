import sys
input = sys.stdin.readline
N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
ans = []

def recur(start):
    global cnt
    if sum(ans) == S and len(ans) > 0:
        cnt += 1
    for i in range(start, N):
        ans.append(num[i])
        recur(i+1)
        ans.pop()
recur(0)
print(cnt)