word = input().upper()
cnt = [0] * 27
# A = 65
for ch in word:
    idx = ord(ch) - ord('A')
    cnt[idx] += 1

max_cnt = max(cnt)
if cnt.count(max_cnt) > 1:
    print("?")
else:
    print(chr(cnt.index(max_cnt) + ord('A')))