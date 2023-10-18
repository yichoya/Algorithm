import sys

V, E = map(int, sys.stdin.readline().split())
edges = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]

def make(x):
    if parent[x] == x:
        return x
    parent[x] = make(parent[x])
    return parent[x]

def union(a, b):
    a = make(a)
    b = make(b)

    if a < b: # 작은 쪽이 부모가 된다. (한 집합 관계라서 부모가 따로 있는 건 아님)
        parent[b] = a
    else:
        parent[a] = b        

def find(a, b):
    return make(a) == make(b)


answer = 0
for a, b, cost in edges:
    # cost가 작은 edge부터 하나씩 추가해가면서 같은 부모를 공유하지 않을 때(사이클 없을 때)만 확정
    if not find(a, b):
        union(a, b)
        answer += cost
print(answer)