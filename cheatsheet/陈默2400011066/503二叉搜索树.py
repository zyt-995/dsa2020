class node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
def insert(root,data):
        if data<root.val:
            if root.left==None:
                root.left = node(data)
            else:
                insert(root.left,data)
        elif data>root.val:
            if root.right==None:
                root.right = node(data)
            else:
                insert(root.right,data)
        return root
def preorder(root):
    ans=[]
    def helper(root):
        if root==None:
            return
        ans.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root)
    return ans
lst=list(map(int,input().split()))
root=node(lst[0])
for i in lst[1:]:
    insert(root,i)
print(" ".join(map(str,preorder(root))))