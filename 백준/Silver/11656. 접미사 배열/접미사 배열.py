import sys

S = sys.stdin.readline().rstrip()
suffix = []
for i in range(len(S)):
    tmp = S[i:]
    suffix.append(tmp)

suffix.sort()
for s in suffix:
    print(s)