def solution(n, lost, reserve):
    new_reserve = sorted(list(set(reserve) - set(lost)))
    new_lost = set(lost) - set(reserve)

    for r in new_reserve:
        # 앞 친구에게 빌려주기
        if r - 1 in new_lost:
            new_lost.remove(r - 1)

        elif r + 1 in new_lost:
            new_lost.remove(r + 1)
            
    return n - len(new_lost)