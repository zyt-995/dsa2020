from collections import deque
class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def insert(root,value):
    if value<root.value:
        if not root.left:
            root.left = node(value)
        else:
            insert(root.left,value)
    if value>root.value:
        if not root.right:
            root.right = node(value)
        else:
            insert(root.right,value)
lst=list(map(int,input().split()))
root=node(lst[0])
for i in range(1,len(lst)):
    insert(root,lst[i])
queue=deque()
queue.append(root)
ans=[]
while queue:
    size = len(queue)
    for _ in range(size):
        q=queue.popleft()
        if q:
            ans.append(q.value)
        if q.left:
            queue.append(q.left)
        if q.right:
            queue.append(q.right)
print(" ".join(map(str,ans)))



