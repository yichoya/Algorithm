import sys

t = int(sys.stdin.readline())
for i in range(t):
	tmp = input().rstrip()
	pwd = []
	sub = []
	for a in tmp:
		if a == '<':
			if pwd:
				sub.append(pwd.pop())
		elif a == '>':
			if sub:
				pwd.append(sub.pop())
		elif a == '-':
			if pwd:
				pwd.pop()
		else:
			pwd.append(a)
	print("".join(pwd),"".join(sub[::-1]),sep="")