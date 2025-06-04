class node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        self.depth=0
def buildtree(inorder,postorder,l):
    if len(inorder)==0:
        return
    if len(inorder)==1:
        r=node(postorder[0])
        r.depth=l
        return r
    r=postorder[-1]
    ind=inorder.index(r)
    root=node(r)
    root.depth=l
    root.left=buildtree(inorder[:ind],postorder[:ind],l+1)
    root.right=buildtree(inorder[ind+1:],postorder[ind:-1],l+1)
    return root
final=[]
def form(root):
    global final
    if root:
        final.append(root.depth*"\t"+root.val)
    if root.left and not root.right:
        form(root.left)
    elif root.left and root.right:
        form(root.left)
        form(root.right)
    elif root.right and not root.left:
         final.append(root.right.depth*"\t"+"*")
         form(root.right)
inorder=input().strip()
postorder=input().strip()
root=buildtree(inorder,postorder,0)
form(root)
for i in final:
    print(i)