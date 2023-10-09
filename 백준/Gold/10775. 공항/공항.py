import sys

# gates[인덱스] = parent
# gates 인덱스 == parent : 비어있음 -> 비행기 주차하고 parent 바꾸기(union)
# gates 인덱스 != parent : 비어있지 않음 -> parent 확인해야함
def find(n):
    if gates[n] == n:
        return n
    else:
        gates[n] = find(gates[n])
        return gates[n]

def union(a, b):
    x = find(a)
    y = find(b)
    gates[x] = y
    return

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
gates = list(range(G + 1))

cnt = 0
for _ in range(P):
    gate = int(sys.stdin.readline())
    # 비행기마다 주차 가능한 게이트 확인
    parent = find(gate)

    if parent == 0: break

    union(parent, parent - 1)
    cnt += 1

print(cnt)