import sys
sys.setrecursionlimit(10 ** 6)

k = int(sys.stdin.readline().rstrip())
tree = [0, 0] + list(map(int, sys.stdin.readline().rstrip().split()))
sz = 2 ** (k + 1)
ans = 0

def dfs(cur):
    global ans
    # 리프 노드일 때
    if cur * 2 >= sz:
        ans += tree[cur]
        return tree[cur]

    # 자식 노드
    left = dfs(cur * 2)
    right = dfs(cur * 2 + 1)

    ans += tree[cur] + abs(left - right)
    return tree[cur] + max(left, right)

dfs(1)
print(ans)