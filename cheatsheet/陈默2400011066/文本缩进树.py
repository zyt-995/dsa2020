class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
stack=[]
level=0
while True:
    s=input().strip()
    k=s.count("/t")
    if k==level+1:
        curr=node(s[-1])
        pre=stack.pop()
        pre.left=curr
        stack.append(pre)
        stack.append(curr)
        level=k
    elif k==level:
        stack.pop()





