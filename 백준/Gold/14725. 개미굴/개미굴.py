import sys
n = int(sys.stdin.readline().rstrip())
data = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dic = {}

def add(li, dic):
    if len(li) == 0:
        return
    if li[0] not in dic:
        dic[li[0]] = {}
    add(li[1:], dic[li[0]])

def printTree(dic, depth):
    keys = sorted(dic.keys())
    for k in keys:
        print("--" * depth + k)
        printTree(dic[k], depth + 1)

for d in data:
    d = d[1:]
    add(d, dic)

printTree(dic, 0)