import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k, n = map(int, input().split())  # k는 보트가 원하는 무게, n은 각 반당 인원
    arr = [list(map(int, input().split())) for _ in range(4)]  # 4 반의 학생들의 몸무게
    arr_1 = []
    arr_2 = []
    for i in range(n):
        for j in range(n):
            arr_1.append(arr[0][i] + arr[1][j])  # 1, 2번째 배열 더하기
            arr_2.append(arr[2][i] + arr[3][j])  # 3, 4번째 배열 더하기
    arr_1.sort()
    arr_2.sort()
    
    start = 0
    end = len(arr_1) - 1
    result = arr_1[start] + arr_2[end]
    while start < len(arr_1) and end >= 0:
        tmp = arr_1[start] + arr_2[end]
        if abs(k - result) > abs(k - tmp):
            result = tmp
        elif abs(k - result) == abs(k - tmp):
            result = min(tmp, result)
        
        if tmp < k:
            start += 1
        elif tmp > k:
            end -= 1
        else:
            break
    print(result)