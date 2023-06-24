while(1):
    string = input()
    if string == ".":
        break

    stack = []
    res = True
    for s in string:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if len(stack)==0 or stack[-1]=="[":
                res = False
                break
            elif stack[-1] == "(":
                stack.pop()
        elif s == "]":
            if len(stack)==0 or stack[-1]=="(":
                res = False
                break
            elif stack[-1] == "[":
                stack.pop()
    if len(stack) == 0 and res == True:
        print("yes")
    else:
        print("no")