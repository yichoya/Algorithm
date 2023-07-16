N = int(input())
N_list = []
rank = []
for i in range(N):
    X = tuple(map(int, input().split()))
    N_list.append(X)
    rank.append(1)

for j in range(len(N_list)):
    for k in range(j+1, len(N_list)):
        if N_list[j][0] > N_list[k][0] and N_list[j][1] > N_list[k][1]:
            rank[k] += 1
        elif N_list[j][0] < N_list[k][0] and N_list[j][1] < N_list[k][1]:
            rank[j] += 1
    
for l in rank:
    print(l, end=' ')