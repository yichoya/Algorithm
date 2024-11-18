# bandage: [시전시간 t, 초당 회복량 x, 추가회복량 y]
# health: 최대 체력
def solution(bandage, health, attacks):
    max_health = health
    attack_dict = {}
    for a in attacks:
        attack_dict[a[0]] = a[1]
    
    t = 0
    continue_sec = 0
    while t <= attacks[-1][0]:
        # 공격
        if t in attack_dict:
            health -= attack_dict[t]
            continue_sec = 0

            if health <=0:
                return -1
        else:
            continue_sec += 1

            if continue_sec < bandage[0]:
                health += bandage[1]
                if health > max_health:
                    health = max_health
            else:
                health = health + bandage[1] + bandage[2]
                if health > max_health:
                    health = max_health
                continue_sec = 0
        t += 1
    return health