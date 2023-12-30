for _ in range(int(input())):
    stack = []
    top = -1
    
    for b in input():
        if b == "(":
            stack.append(b)
            top += 1
        elif b ==")":
            if top < 0:
                stack.append(b)
                break
            if stack[top] == "(":
                stack.pop()
                top -= 1
            else:
                stack.append(b)
                top += 1
        
    if len(stack) <= 0:
        print("YES")
    else:
        print("NO")