n = int(input())
m = int(input())

# 컴퓨터 연결 상태를 2차원 리스트로 저장
# 컴퓨터의 번호를 인덱스로 사용하기 위해 길이를 n + 1로 설정
data = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * (n + 1)
res = 0

def dfs(start):
    global res
    visited[start] = True
    for i in data[start]:
        if visited[i] == False:
            dfs(i)
            res += 1

dfs(1)
print(res)