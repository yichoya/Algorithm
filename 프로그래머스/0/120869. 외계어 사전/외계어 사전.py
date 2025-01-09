def solution(spell, dic):
    n = len(spell)
    visited = [0] * n
    flag = 0
    
    def recur(res):
        nonlocal flag
        if len(res) == n:
            if res in dic:
                flag = 1
            return
        for i in range(n):
            if visited[i]: continue
            visited[i] = 1
            recur(res + spell[i])
            visited[i] = 0
    
    recur("")
    return 1 if flag else 2