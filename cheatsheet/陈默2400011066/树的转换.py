from collections import deque


class node:
    def __init__(self):
        self.next = []
        self.left = None
        self.right = None
def buildtree(s):
    stack=[]
    stack.append(node())
    for i in s:
        if i=="d":
            curr=stack.pop()
            k=node()
            curr.next.append(k)
            if len(curr.next)==1:
                curr.left=k
            if len(curr.next)>=2:
                curr.next[-2].right=k
            stack.append(curr)
            stack.append(k)
        if i=="u":
            stack.pop()
    #h1
    h1=0
    root=stack.pop()
    queue=deque([(root,0)])
    while queue:
        curr,h=queue.popleft()
        for i in curr.next:
            queue.append((i,h+1))
        if curr.next:
            h1=max(h1,h+1)
    q=deque([(root,0)])
    h2=0
    while q:
        curr,h=q.popleft()
        if curr.left:
            q.append((curr.left,h+1))
        if curr.right:
            q.append((curr.right,h+1))
        if curr.left or curr.right:
            h2=max(h2,h+1)
    return h1,h2
seq=0
while True:
    s=input()
    if s=="#":
        break
    seq+=1
    h1,h2=buildtree(s)
    print(f"Tree {seq}: {h1} => {h2}")


