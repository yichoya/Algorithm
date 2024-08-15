import sys

n = int(sys.stdin.readline())
lines = [int(sys.stdin.readline()) for _ in range(n)]
storage = set(lines)
ans = 0

for s in storage:
    cnt = 0
    prev = lines[0]
    tmp = -1e9
    for i in range(n):
        if lines[i] == s: continue
        if prev == s or prev != lines[i]:
            prev = lines[i]
            cnt = 1
            continue
        if prev == lines[i]:
            cnt += 1
        tmp = max(tmp, cnt)
    ans = max(ans, tmp)
print(ans)