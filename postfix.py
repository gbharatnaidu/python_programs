def evall(a):
    stack = []
    for i in range(len(a)):
        if  a[i]== "+":
            stack.append(stack.pop() + stack.pop())
        elif a[i] == "-":
            z=stack.pop()
            stack.append(stack.pop() -z)
        elif a[i] == '*':
            stack.append(stack.pop() * stack.pop())
        elif a[i] =='/':
            l=stack.pop()
            stack.append(stack.pop() / l)
        elif a[i] in "0123456789":
                stack.append(int(a[i]))
    return stack.pop()
print(evall("1295-+*"))
