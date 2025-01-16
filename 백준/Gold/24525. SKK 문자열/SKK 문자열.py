import sys
from collections import defaultdict

string = sys.stdin.readline().strip()
length = len(string)
prefix = [0] * (length + 1)
cnt_S = [0] * (length + 1)
cnt_K = [0] * (length + 1)

for i in range(1, length + 1):
    c = string[i - 1]
    prefix[i] = prefix[i - 1]
    cnt_S[i] = cnt_S[i - 1]
    cnt_K[i] = cnt_K[i - 1]

    if c == 'S':
        prefix[i] += 2
        cnt_S[i] += 1
    elif c == 'K':
        prefix[i] -= 1
        cnt_K[i] += 1

prefix_map = defaultdict(lambda: float('inf'))
for i in range(length + 1):
    prefix_map[prefix[i]] = min(prefix_map[prefix[i]], i)

answer = -1

for i in range(1, length + 1):
    min_idx = prefix_map[prefix[i]]

    tmp = i - min_idx
    cnt_s = cnt_S[i] - cnt_S[min_idx]
    cnt_k = cnt_K[i] - cnt_K[min_idx]

    if cnt_s != 0 and cnt_k != 0:
        answer = max(answer, tmp)

print(answer)