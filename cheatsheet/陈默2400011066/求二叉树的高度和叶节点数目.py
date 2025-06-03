from collections import deque
class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
nodes={}
n=int(input())
gen=[True]*n
for i in range(n):
    if i not in nodes:
        nodes[i]=node(i)
    a,b=map(int,input().split())
    if a!=-1 and a not in nodes:
        nodes[a]=node(a)
    if b!=-1 and b not in nodes:
        nodes[b]=node(b)
    if a!=-1:
        nodes[i].left=nodes[a]
        gen[a]=False
    if b!=-1:
        nodes[i].right=nodes[b]
        gen[b]=False
leaf=0
root=nodes[gen.index(True)]
queue=deque()
queue.append((root,0))
height=0
leaf=0
while queue:
    currnode,h=queue.popleft()
    height=max(height,h)
    if currnode.left:
        queue.append((currnode.left,h+1))
    if currnode.right:
        queue.append((currnode.right,h+1))
    if not currnode.left and not currnode.right:
        leaf+=1
if n==0:
    print(0,0)
else:
    print(height,leaf)


