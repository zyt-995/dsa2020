flag="NO"
ERROR=False
stack=[]
s=input()
for i in s:
    if i in ["(","[","{"]:
        if stack:
            flag="YES"
        stack.append(i)
    elif i in [")","]","}"]:
        if not stack:
            ERROR=True
            break
        k=stack.pop()
        if i==")" and k!="(":
            ERROR=True
            break
        elif i=="]" and k!="[":
            ERROR=True
            break
        elif i=="}" and k!="{":
            ERROR=True
            break
if ERROR:
    print("ERROR")
else:
    print(flag)

