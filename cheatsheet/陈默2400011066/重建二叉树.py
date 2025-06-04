def postorder(preorder,inorder):
    if not inorder:
        return ""
    if len(inorder)==1:
        return preorder
    r=preorder[0]
    ind=inorder.index(r)
    left=postorder(preorder[1:ind+1],inorder[:ind])
    right=postorder(preorder[ind+1:],inorder[ind+1:])
    return left+right+r
while True:
     try:
        preorder,inorder=map(str,input().split())
        print(postorder(preorder,inorder))
     except EOFError:
            break
