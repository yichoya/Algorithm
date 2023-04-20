T = int(input())
tmp = []
for _ in range(T):
    N, S = input().split()
    tmp.append([N, S])
    
for t in tmp:
    res = ''
    for i in t[1]:
        res += i * int(t[0])
    print(res)