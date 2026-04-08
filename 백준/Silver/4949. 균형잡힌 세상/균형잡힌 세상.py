while True:
    s = input()

    if s == ".":
        break

    stack = []
    balanced = True

    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)

        elif ch == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()

        elif ch == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()

    if stack:
        balanced = False

    if balanced:
        print("yes")
    else:
        print("no")