from collections import deque
class node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
def build(inorder,postorder):
    if len(inorder)==0:
        return
    if len(inorder)==1:
        return node(inorder[0])
    r=postorder[-1]
    ind=inorder.index(r)
    root=node(r)
    root.left=build(inorder[:ind],postorder[:ind])
    root.right=build(inorder[ind+1:],postorder[ind:-1])
    return root
def levelorder(root):
    queue=deque()
    queue.append(root)
    level=[]
    while queue:
        l=len(queue)
        for i in range(l):
            node=queue.popleft()
            if node:
                level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return level
n=int(input())
for i in range(n):
    inorder=input().strip()
    postorder=input().strip()
    root=build(inorder,postorder)
    print("".join(map(str,levelorder(root))))