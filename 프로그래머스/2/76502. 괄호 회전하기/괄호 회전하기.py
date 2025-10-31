from collections import deque

def check_str(s):
    stack = deque()
    pairs = {')': '(', '}': '{', ']': '['}
    
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != pairs[ch]:
                return 0
            stack.pop()
    
    if not stack:
        return 1
    else:
        return 0
        
    
    
def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        string = s[i:] + s[0:i]
        answer += check_str(string)
    
    return answer