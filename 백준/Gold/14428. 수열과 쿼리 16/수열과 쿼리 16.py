import sys

n = int(sys.stdin.readline().rstrip())
arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

inf = 1234567890
sz = 4 * (n + 1)
tree = [(inf, inf)] * sz
def build(node, start, end):
    if start == end:
        tree[node] = (arr[start], start)
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)

        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def update(idx, value, node, start, end):
    # idx가 start ~ end 범위에 들어가면 해당 노드를 갱신

    if start == end:
        tree[node] = (value, idx)
        return

    mid = (start + end) // 2
    # 트리는 구간을 이진 분할해서 관리하기 때문에
    # 값 하나만 바꿀 때는 정확히 그 위치만 갱신하고
    # 그 위로 올라가며 부모 노드를 다시 계산해야한다.
    if idx <= mid:
        update(idx, value, node * 2, start, mid)
    else:
        update(idx, value, node * 2 + 1, mid + 1, end)

    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(node, start, end, left, right):
    # start ~ end: 해당 노드가 담당하는 구간
    # left ~ right: 찾아야 하는 구간

    if right < start or end < left:
        return (inf, inf)

    # [start, end]가 [left, right]에 완전히 포함되는 경우
    if left <= start and end <= right:
        return tree[node]

    # [start, end]와 [l, r]이 일부만 겹치는 경우
    mid = (start + end) // 2
    left_res = query(node * 2, start, mid, left, right)
    right_res = query(node * 2 + 1, mid + 1, end, left, right)
    return min(left_res, right_res)


build(1, 1, n)
for _ in range(m):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    if cmd[0] == 1:
        update(cmd[1], cmd[2], 1, 1, n)
    else:
        print(query(1, 1, n, cmd[1], cmd[2])[1])
