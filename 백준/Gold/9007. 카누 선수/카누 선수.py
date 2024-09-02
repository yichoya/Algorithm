import sys
t = int(sys.stdin.readline())
for _ in range(t):
    k, n = map(int, sys.stdin.readline().split())
    weights = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

    # weightsA: class1, class2에서 조합할 수 있는 몸무게의 합
    # weightsB: class3, class4에서 조합할 수 있는 몸무게의 합
    weightsA, weightsB = [], []
    for i in range(n):
        for j in range(n):
            weightsA.append(weights[0][i] + weights[1][j])
            weightsB.append(weights[2][i] + weights[3][j])
    weightsA.sort()
    weightsB.sort()

    start, end = 0, n**2 - 1
    res = weightsA[start] + weightsB[end]
    while start < n**2 and end > -1:
        tmp = weightsA[start] + weightsB[end]
        # 절대값이 같은 경우 -> 더 작은값 채택
        if abs(k - tmp) == abs(k - res):
            res = min(res, tmp)
        elif abs(k - tmp) < abs(k - res):
            res = tmp

        if tmp < k:
            start += 1
        elif tmp > k:
            end -= 1
        else:
            break
    print(res)