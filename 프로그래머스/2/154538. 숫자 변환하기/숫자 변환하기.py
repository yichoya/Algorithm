
# def recur(cur, cnt):
#     global answer
    
#     if cur == y:
#         answer = min(answer, cnt)
#         return

#     if cur > y:
#         return

#     recur(cur + n, cnt + 1)
#     recur(cur * 2, cnt + 1)
#     recur(cur * 3, cnt + 1)

# def recur(cur, y, n, dp):
    
#     if cur == y:
#         return 0

#     if cur > y:
#         return 1234567890
    
#     if dp[cur] != -1:
#         return dp[cur]
    
#     tmp = 1234567890
#     tmp = min(tmp, recur(cur + n, y, n, dp) + 1)
#     tmp = min(tmp, recur(cur * 2, y, n, dp) + 1)
#     tmp = min(tmp, recur(cur * 3, y, n, dp) + 1)
    
#     dp[cur] = tmp
#     return dp[cur]
    

def solution(x, y, n):

#     dp = [-1] * (y + 1)
#     answer = recur(x, y, n, dp)
    
#     if answer == 1234567890:
#         return -1
#     else:
#         return answer

    dp = [float('inf')] * (y + 1)
    dp[x] = 0
    
    for i in range(x, y + 1):
        # 아직 값이 없으면 스킵
        if dp[i] == float('inf'):
            continue

        # 가능한 연산 3가지 적용
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    
    if dp[y] == float('inf'):
        return -1
    else:
        return dp[y]


