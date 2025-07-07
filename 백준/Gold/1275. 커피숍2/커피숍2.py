import sys

n, q = map(int, sys.stdin.readline().split())
li = [0] + list(map(int, sys.stdin.readline().split()))

sz = 4 * (n + 1)
tree = [0] * sz

def build(node, start, end):
    if start == end:
        tree[node] = li[start]
        return

    mid = (start + end) // 2
    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(left, right, node, start, end):
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    l_child = query(left, right, node * 2, start, mid)
    r_child = query(left, right, node * 2 + 1, mid + 1, end)
    return l_child + r_child


def update(target, value, node, start, end):
    if target < start or end < target:
        return

    if start == end:
        li[target] = value
        tree[node] = value
        return

    mid = (start + end) // 2
    update(target, value, node * 2, start, mid)
    update(target, value, node * 2 + 1, mid + 1, end)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]



build(1, 1, n)
for _ in range(q):
    x, y, a, b = map(int, sys.stdin.readline().split())
    left, right = min(x, y), max(x, y)
    print(query(left, right, 1, 1, n))
    update(a, b, 1, 1, n)

