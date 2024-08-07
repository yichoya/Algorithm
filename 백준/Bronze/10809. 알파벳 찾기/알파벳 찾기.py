import sys
text = str(sys.stdin.readline().rstrip())
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for a in alpha:
    if a in text:
        print(text.find(a), end=" ")
    else: print(-1, end=" ")