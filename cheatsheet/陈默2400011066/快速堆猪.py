stack=[]
while True:
  try:
    command=list(map(str,input().split()))
    if command[0]=="pop":
        if stack:
            stack.pop()
    if command[0]=="push":
        if not stack:
            stack.append(int(command[1]))
        else:
            stack.append(min(int(command[1]),stack[-1]))
    if command[0]=="min":
        if stack:
            print(stack[-1])
  except EOFError:
      break
