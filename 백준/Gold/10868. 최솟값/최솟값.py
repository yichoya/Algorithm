import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(n)]

sz = 4 * (n + 1)
inf = 1234567890
tree = [inf] * sz

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]

    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)

        tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(left, right, node, start, end):
    # left ~ right: 찾아야 하는 구간
    # start ~ end: 해당 노드가 담당하는 구간

    if right < start or end < left:
        return inf

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_min = query(left, right, node * 2, start, mid)
    right_min = query(left, right, node * 2 + 1, mid + 1, end)
    return min(left_min, right_min)



build(1, 1, n)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(query(a, b, 1, 1, n))