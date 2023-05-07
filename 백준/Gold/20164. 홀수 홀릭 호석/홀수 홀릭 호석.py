import math
N = input()

maxCnt = 0
minCnt = math.inf

def oddCount(n:str):
    cnt = 0
    for i in N:
        if i in '13579':
            cnt += 1
    return cnt

def oddHolic(n:str, cnt:int):
    global maxCnt, minCnt
    if len(n) == 1:
        maxCnt = max(cnt, maxCnt)
        minCnt = min(cnt, minCnt)
    elif len(n) == 2:
        newN = str(int(n[0]) + int(n[1]))
        cnt += oddCount(newN)
        oddHolic(newN, cnt)
    else:
        for i in range(len(n) - 2):
            for j in range(i + 1, len(n) - 1):
                x = n[:i+1]
                y = n[i+1:j+1]
                z = n[j+1:]
                newN = str(int(x) + int(y) + int(z))
                cnt += oddCount(newN)
                oddHolic(newN, cnt)

oddHolic(N, oddCount(N))
print(minCnt, maxCnt)