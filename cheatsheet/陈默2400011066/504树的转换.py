class node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None#为什么要有parent,是为了找兄弟
        self.depth=0
        self.children=[]
        self.postbro=None
root = node()
s=input()
stack=[]
nodes=[]
stack.append(root)
nodes.append(root)
for i in s:
    if i=="d":
        parent=stack[-1]
        temp=node()
        parent.children.append(temp)
        temp.parent=parent
        temp.depth=parent.depth+1
        if len(parent.children)>=2:
            parent.children[-2].postbro=temp
        stack.append(temp)
        nodes.append(temp)
    elif i=="u":
        stack.pop()
for node in nodes:
    if node.children:
        node.left=node.children[0]
    if node.postbro:
        node.right=node.postbro
h1=max(node.depth for node in nodes)
#要计算树的高度，都通过后序遍历计算
maxdepth={}
postorder=[]
curr=root
while True:
    while curr:
        postorder.append((curr,False))
        curr=curr.left
    if not postorder:#curr就是None
        break
    node,processed=postorder.pop()#这时候第一个pop的肯定是叶子节点
    if not processed:#右子树还没处理，重新入栈
        postorder.append((node,True))
        curr=node.right
    else:
        leftdepth=maxdepth.get(node.left,0)
        rightdepth=maxdepth.get(node.right,0)
        currdepth=max(leftdepth,rightdepth)+1
        maxdepth[node]=currdepth
h2=maxdepth.get(root,0)-1
print(f"{h1} => {h2}")





