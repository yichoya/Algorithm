import sys

word = sys.stdin.readline().rstrip()

check = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0
tmp = ""

for c in check:
    word = word.replace(c, 'a')

print(len(word))