def solution(info, n, m):
    INF = 1234567890
    answer = 0
    sz = len(info)
    
    # dp[i][b]: i번째 물건 훔칠 때 B가 남긴 흔적이 b 인 상태에서의 A의 최소 흔적
    dp = [[INF] * 120 for _ in range(sz + 1)]
    dp[0][0] = 0
    
    for i in range(1, sz + 1):
        cost_a, cost_b = info[i - 1]
        for b in range(m):
            if dp[i - 1][b] == INF:
                continue
            
            # a가 훔쳤을 때
            new_a = dp[i - 1][b] + cost_a
            if new_a < n:
                dp[i][b] = min(dp[i][b], new_a)

            # b가 훔쳤을 때
            new_b = b + cost_b
            if new_b < m:
                dp[i][new_b] = min(dp[i][new_b], dp[i - 1][b])
        
    answer = min(dp[sz][b] for b in range(m))
    if answer == INF:
        return -1
    else:
        return answer