import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = [0] + list(int(sys.stdin.readline().rstrip()) for _ in range(n))
sz = 4 * (n + 1)
tree = [0] * sz
MOD = 1000000007

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)

        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD


def update(index, value, cur, start, end):
    # cur: 현재 노드의 인덱스
    if start == end:
        arr[index] = value
        tree[cur] = value
        return

    mid = (start + end) // 2
    if index <= mid:
        update(index, value, cur * 2, start, mid)
    else:
        update(index, value, cur * 2 + 1, mid + 1, end)

    tree[cur] = (tree[cur * 2] * tree[cur * 2 + 1]) % MOD


# 쿼리 구간 [left, right] 안에 포함된 구간들의 곱 구하기
def query(left, right, cur, start, end):
    # 범위를 벗어나는 경우
    if right < start or end < left:
        return 1

    # 범위에 딱 맞는 경우(쿼리 범위에 현재 노드가 완전히 포함될 때)
    if left <= start and end <= right:
        return tree[cur]

    # 범위가 걸친 경우
    mid = (start + end) // 2
    left_value = query(left, right, cur * 2, start, mid)
    right_value = query(left, right, cur * 2 + 1, mid + 1, end)
    return (left_value * right_value) % MOD


build(1, 1, n)
for _ in range(m + k):
    cmd = list(map(int, sys.stdin.readline().split()))
    if cmd[0] == 1:
        update(cmd[1], cmd[2], 1, 1, n)
    else:
        print(query(cmd[1], cmd[2], 1, 1, n))