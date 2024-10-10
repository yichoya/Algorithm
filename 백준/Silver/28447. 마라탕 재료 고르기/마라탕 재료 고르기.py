import sys

def recur(start, malatang):
    global total

    if k == 1:
        total = 0
        return
    if len(malatang) == k:
        tmp = 0
        for a in range(0, k - 1):
            for b in range(a + 1, k):
                tmp += match[malatang[a]][malatang[b]]
        total = max(total, tmp)
        return
    for i in range(start, n):
        malatang.append(i)
        recur(i + 1, malatang)
        malatang.pop()


n, k = map(int, sys.stdin.readline().split())
match = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
total = -1234567890
recur(0, [])
print(total)