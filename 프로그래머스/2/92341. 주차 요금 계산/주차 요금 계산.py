import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    parking = dict()
    total = defaultdict(int)
    
    def time_to_min(time_str):
        hour, minute = map(int, time_str.split(':'))
        return hour * 60 + minute

    for record in records:
        time_str, num, state = record.split()
        time = time_to_min(time_str)
        
        if state == 'IN':
            parking[num] = time
        else:
            in_time = parking.pop(num)
            total[num] += time - in_time
    
    for num, time in parking.items():
        total[num] += time_to_min('23:59') - time
    
    basic_time, basic_fee, unit_time, unit_fee = fees
    for num in sorted(total.keys()):
        total_time = total[num]
        if total_time > basic_time:
            tmp = basic_fee + math.ceil((total_time - basic_time) / unit_time) * unit_fee
            answer.append(tmp)
        else:
            answer.append(basic_fee)
    
            
    return answer