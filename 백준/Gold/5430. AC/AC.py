import sys
from collections import deque

T =  int(sys.stdin.readline().strip())
res = []
for _ in range(T):
    cmd = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()[1:-1].replace(",", " ").split()
    cnt = 0
    flag = True
    
    arr = deque(arr)
    # print(arr, len(arr))

    for i in cmd:
        if i == 'R':
            cnt += 1
        else:
            if len(arr) == 0:
                res.append("error")
                flag = False
                break
            else:
                if cnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    if flag:
        if cnt % 2 == 0:
            tmp = "[" + ",".join(arr) + "]"
            # print(tmp)
            res.append(tmp)
        else:
            arr.reverse()
            tmp = "[" + ",".join(arr) + "]"
            # print(tmp)
            res.append(tmp)
    
for i in res:
    print(i)

