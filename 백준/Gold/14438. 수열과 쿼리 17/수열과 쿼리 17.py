import sys

n = int(sys.stdin.readline().rstrip())
arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

inf = 1234567890
sz = 4 * (n + 1)
tree = [inf] * sz


def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def update(target, value, node, start, end):
    if target < start or target > end:
        return

    if start == end:
        arr[target] = value
        tree[node] = value
        return

    mid = (start + end) // 2
    update(target, value, node * 2, start, mid)
    update(target, value, node * 2 + 1, mid + 1, end)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(left, right, node, start, end):
    if right < start or end < left:
        return inf

    if left <= start and end <= right:
        return tree[node]

    # 범위가 걸친 경우
    mid = (start + end) // 2
    left_min = query(left, right, node * 2, start, mid)
    right_min = query(left, right, node * 2 + 1, mid + 1, end)
    return min(left_min, right_min)


build(1, 1, n)
for _ in range(m):
    cmd, a, b = map(int, sys.stdin.readline().rstrip().split())
    if cmd == 1:
        update(a, b, 1, 1, n)
    else:
        print(query(a, b, 1, 1, n))
