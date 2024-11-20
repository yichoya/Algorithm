def solution(id_list, report, k):
    report_list = {id: [] for id in id_list}
    report_cnt = {id: 0 for id in id_list}
    mail_cnt = {id: 0 for id in id_list}
    
    for r in set(report):
        a, b = r.split()
        report_list[a].append(b)
        report_cnt[b] += 1
    
    for id, cnt in report_cnt.items():
        if cnt >= k:
            for user in id_list:
                if id in report_list[user]:
                    mail_cnt[user] += 1
    
    answer = list(mail_cnt.values())
    return answer