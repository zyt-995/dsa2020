'''
描述
给定一棵二叉树的前序遍历和中序遍历的结果，求其后序遍历。

输入
输入可能有多组，以EOF结束。
每组输入包含两个字符串，分别为树的前序遍历和中序遍历。每个字符串中只包含大写字母且互不重复。
输出
对于每组输入，用一行来输出它后序遍历结果。
样例输入
DBACEGF ABCDEFG
BCAD CBAD
样例输出
ACBFGED
CDAB
'''
def GetPostorder(Preorder,Inorder):
    if len(Preorder)<=1:
        return Preorder
    else:
        root=Preorder[0]
        rootPos=Inorder.index(root)
        return GetPostorder(Preorder[1:rootPos+1],Inorder[:rootPos])+GetPostorder(Preorder[rootPos+1:],Inorder[rootPos+1:])+root
    

try:
    while True:
        a,b=list(input().split())
        print(GetPostorder(a,b))
except:
    pass

