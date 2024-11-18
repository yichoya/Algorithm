def time_to_sec(string):
    min, sec = map(int, string.split(':'))
    return min * 60 + sec

def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_sec(video_len)
    pos = time_to_sec(pos)
    op_start = time_to_sec(op_start)
    op_end = time_to_sec(op_end)
    
    if op_start <= pos <= op_end:
            pos = op_end
    for cmd in commands:
        if cmd == 'next': pos += 10
        else: pos -= 10 
        
        if pos > video_len:
            pos = video_len
        elif pos < 0:
            pos = 0
            
        if op_start <= pos <= op_end:
            pos = op_end
            
    res = [pos // 60, pos % 60]
    answer = ':'.join(map(lambda x: str(x) if x >= 10 else '0' + str(x), res))
    return answer