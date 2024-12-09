from collections import Counter

def solution(k, tangerine):
    tangerine_cnt = Counter(tangerine)
    li = sorted(tangerine_cnt.values(), reverse=True)
    answer = 0
    cnt = 0
    
    for i in li:
        if cnt < k:
            cnt += i
            answer += 1
        else: break
    return answer