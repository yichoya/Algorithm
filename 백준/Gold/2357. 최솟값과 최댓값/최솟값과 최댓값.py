import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(n)]
size = 4 * n
min_tree = [0] * size
max_tree = [0] * size

def build(node, start, end):
    if start == end:
        min_tree[node] = arr[start]
        max_tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)   # 왼쪽 자식 노드
        build(node * 2 + 1, mid + 1, end)   # 오른쪽 자식 노드

        # 현재 노드 채우기
        min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
        max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])

def query(node, start, end, l, r):
    # 노드 범위 밖인 경우
    if r < start or end < l:
        return (1234567890, -1234567890)

    # 노드의 범위에 들어가는 경우
    if l <= start and end <= r:
        return (min_tree[node], max_tree[node])

    # 노드 두 개의 범위에 걸친 경우
    mid = (start + end) // 2
    left_query = query(node * 2, start, mid, l, r)
    right_query = query(node * 2 + 1, mid + 1, end, l, r)

    return (
        min(left_query[0], right_query[0]),
        max(left_query[1], right_query[1])
    )


build(1, 1, n)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    res = query(1, 1, n, a, b)
    print(res[0], res[1])
