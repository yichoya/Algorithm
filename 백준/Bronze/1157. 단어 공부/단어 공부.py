word = input().upper()
check = list(set(word))

total = []

for i in check:
    if i in word:
        tmp = word.count(i)
        total.append(tmp)

M = max(total)
if M >= 2 and total.count(M) >= 2:
    print('?')
else: print(check[total.index(M)])