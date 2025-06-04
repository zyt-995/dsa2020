class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def preorder(root):
    ans=[]
    def helper(root):
        if root is None:
            return
        ans.append(root.value)
        if root.left:
            helper(root.left)
        if root.right:
            helper(root.right)
    helper(root)
    return " ".join(map(str,ans))

def insert(root,data):
    if data<root.value:
        if not root.left:
            root.left = node(data)
        else:
            insert(root.left,data)
    if data>root.value:
        if not root.right:
            root.right = node(data)
        else:
            insert(root.right,data)
    return root
lst=list(map(int,input().split()))
root=node(lst[0])
for i in range(1,len(lst)):
    insert(root,lst[i])
print(preorder(root))
