class Tree:
    def __init__(self,data,left=None,right=None,father=None):
        self.data=data
        self.left,self.right=left,right
        self.father=father
    def addleft(self,tree):
        self.left=tree
        self.left.father=self
    def addright(self,tree):
        self.right=tree
        self.right.father=self
def buildtree(s):#对于完全二叉树来说，可以这样建立树，也就是通过数学手段，而不要用指针的方式
    l=len(s)
    nodes=[None]*(l+1)
    nodes[0]=None
    for i in range(1,l+1):
        nodes[i]=Tree(int(s[i-1]))
    for i in range(1,l+1):
        left=2*i
        right=2*i+1
        if left<=l:
            nodes[i].addleft(nodes[left])
        if right<=l:
            nodes[i].addright(nodes[right])
    return nodes[1]
#这是一种有趣的新型动态规划，通过递归的手段维护了两个信息
def find(root):#本题目核心，动态规划，需要嵌套函数。内层函数可以维护一个节点两种状态，采用元组的形式
    def help(node):#对于一个节点操作
        if not node:
            return(0,0)#前者是拿走这个节点，后者是不拿这个节点，相当于给每个节点赋了两个值，便于操作
        left=help(node.left)
        right=help(node.right)
        rob=node.data+left[1]+right[1]
        notrob=max(left)+max(right)
        return (rob,notrob)
    return max(help(root))
a=int(input())
s=input().split()
root=buildtree(s)
print(find(root))

