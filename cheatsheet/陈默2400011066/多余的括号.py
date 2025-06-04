def purify(s):
    num=[]
    op=[]
    priority=[]
    base=0
    for i in s:
        if i=="(":
            base+=1
        elif i==")":
            base-=1
        elif i.isdigit():
            num.append(i)
        elif i=="+":
            op.append(i)
            priority.append(base)
        else:
            op.append(i)
            priority.append(base+1)
    helper=priority.sort()
    for i in range(len(op)):
        pri=

