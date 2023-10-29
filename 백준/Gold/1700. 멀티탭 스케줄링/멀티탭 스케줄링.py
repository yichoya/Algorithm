N, K = map(int, input().split())

order = list(map(int, input().split()))

use = [False] * 101
put = 0
ans = 0

for i in range(K):
    temp = order[i]

    if not use[temp]:  # 콘센트가 꽂혀있지 않은 경우
        if put < N:  # 콘센트를 꽂을 공간이 있는 경우
            use[temp] = True
            put += 1
        else:  # 콘센트를 꽂을 공간이 없는 경우
            arrList = []
            for j in range(i, K):
                if use[order[j]] and order[j] not in arrList:
                    arrList.append(order[j])

            if len(arrList) != N:  # 나중에도 사용되는 콘센트가 구멍의 개수보다 작을 경우
                for j in range(len(use)):
                    if use[j] and j not in arrList:
                        use[j] = False
                        break
            else:  # 현재 꽂혀 있는 모든 콘센트가 나중에도 사용될 경우
                remove = arrList[-1]  # 가장 마지막에 사용될 콘센트를 제거
                use[remove] = False

            use[temp] = True
            ans += 1

print(ans)