def is_available(park, mat, x, y):
    for r in range(x, x + mat):
        for c in range(y, y + mat):
            if park[r][c] != "-1":
                return False
    return True
        
    
def solution(mats, park):
    w = len(park[0])
    h = len(park)
    mats.sort(reverse=True)
    for mat in mats:
        for x in range(0, h - mat + 1):
            for y in range(w - mat + 1):
                # if x + mat >= h or y + mat >= w:
                #     break
                if is_available(park, mat, x, y):
                    return mat
    return -1