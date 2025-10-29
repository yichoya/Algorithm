# def solution(orders, course):
#     answer = []
#     return answer

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    result = []

    for c in course:
        freq = defaultdict(int)
        for order in orders:
            order = ''.join(sorted(order))
            for comb in combinations(order, c):
                comb_str = ''.join(comb)
                freq[comb_str] += 1

        if not freq:
            continue

            
        max_freq = max(freq.values())
        
        # 2회 이상 등장해야함
        if max_freq < 2:
            continue

        for key, val in freq.items():
            if val == max_freq:
                result.append(key)

    # 오름차순 정렬
    return sorted(result)
