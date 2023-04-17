L, C = map(int, input().split())
char = sorted(input().split())

def isPassword(pw):
    vol = 0
    con = 0
    for i in pw:
        if i in 'aeiou':
            vol += 1
        else: con += 1
    if vol >= 1 and con >= 2:
        # print(*pw)
        print(''.join(pw))

def createWord(start, word):
    if len(word) == L:
        isPassword(word)
        return
    for i in range(start, C):
        word.append(char[i])
        createWord(i + 1, word)
        word.pop()

createWord(0, [])