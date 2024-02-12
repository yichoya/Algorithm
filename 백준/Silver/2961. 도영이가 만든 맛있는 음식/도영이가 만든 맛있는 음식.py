import sys

n = int(sys.stdin.readline())
taste = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [False] * n
diff = int(1e9)
def recur(start, S, B):
    global diff
    if B != 0:
        diff = min(diff, abs(S-B))

    for i in range(start, n):
        if not visit[i]:
            visit[i] = True
            recur(start + 1, S * taste[i][0] , B + taste[i][1])
            #recur(start + 1, S, B)
            visit[i]=False
recur(0, 1, 0)
print(diff)