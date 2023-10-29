import sys
N, K = map(int, sys.stdin.readline().split())
electrics = list(map(int, sys.stdin.readline().split()))
multitaps = [False] * (K + 1)
res, cnt = 0, 0 # cnt: 멀티탭에 꽂혀있는 기기의 갯수

for i, v in enumerate(electrics):
    # 사용하려는 기기가 멀티탭에 꽂혀있지 않은 경우
    if not multitaps[v]:
        if cnt < N:  # 멀티탭에 꽂을 수 있다면
            multitaps[v] = True
            cnt += 1
        else: 
            checkList = []
            for j in range(i, K):
                if multitaps[electrics[j]] and electrics[j] not in checkList:
                    checkList.append(electrics[j])

            # 현재 꽂혀 있는 모든 콘센트가 나중에도 사용될 경우
            if len(checkList) == N:  
                # 가장 마지막에 사용될 콘센트를 제거
                multitaps[checkList[-1]] = False
            else:
                for j in range(len(multitaps)):
                    if multitaps[j] and j not in checkList:
                        multitaps[j] = False
                        break

            multitaps[v] = True
            res += 1
print(res)