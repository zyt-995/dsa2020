from collections import deque
class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
n=int(input())
nodes={}
for i in range(1,n+1):
    a,b=map(int,input().split())
    for j in [a,b,i]:
        if j not in nodes and j!=-1:
            nodes[j] = node(j)
    if a!=-1:
       nodes[i].left = nodes[a]
    if b!=-1:
        nodes[i].right = nodes[b]
root=nodes[1]
queue=deque([(root,1)])
dep=1
while queue:
    curr,depth=queue.popleft()
    if curr.left:
        queue.append((curr.left,depth+1))
        dep=max(dep,depth+1)
    if curr.right:
        queue.append((curr.right,depth+1))
        dep=max(dep,depth+1)
print(dep)

