import sys, math
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

nums2 = sorted(nums)

avg = round(sum(nums2) / len(nums2))
med = nums2[int(N / 2)]
rng = max(nums2) - min(nums2)

def mode(li):
    if len(li) == 1:
        return li[0]
    tmp = Counter(li).most_common()
    tmp.sort(key=lambda x:(-x[1], x[0]))
    if tmp[0][1] == tmp[1][1]:
        res = tmp[1][0]
    else:
        res = tmp[0][0]
    return res


print(avg)
print(med)
print(mode(nums))
print(rng)
