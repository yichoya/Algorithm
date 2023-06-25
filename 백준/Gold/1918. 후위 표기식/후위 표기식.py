import sys

formula = sys.stdin.readline().rstrip()
stack = []

for f in formula:
    if f >= "A" and f <= "Z":
        print(f, end="")
    elif f == "(":
        stack.append(f)
    elif f == ")":
        while (stack and stack[-1] != "("):
            print(stack.pop(), end="")
        stack.pop()
    elif (f == "+" or f == "-"):
        while(stack and stack[-1]!="("):
            print(stack.pop(), end="")
        stack.append(f)
    elif (f == "*" or f == "/"):
        while(stack and stack[-1]!="(" and (stack[-1] == "*" or stack[-1] == "/")):
            print(stack.pop(), end="")
        stack.append(f)

if stack:
    for _ in range(len(stack)):
        print(stack.pop(), end="")