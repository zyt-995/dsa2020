def isfloat(v):
    try:
        float(v)
        return True
    except ValueError:
        return False
s=list(map(str,input().split()))
stack=[]
for i in s[::-1]:
    if isfloat(i):
        stack.append(float(i))
    else:
        a=stack.pop()
        b=stack.pop()
        if i=="+":
            stack.append(a+b)
        if i=="*":
            stack.append(a*b)
        if i=="-":
            stack.append(a-b)
        if i=="/":
            stack.append(a/b)
print(f"{stack[0]:.6f}")

