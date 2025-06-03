s=input().strip()
stack=[]
for i in s:
    stack.append(i)
    if len(stack)>2 and i=="U":
        if stack[-3:]==["P","K","U"]:
            stack.pop()
            stack.pop()
            stack.pop()
print("".join(stack))
