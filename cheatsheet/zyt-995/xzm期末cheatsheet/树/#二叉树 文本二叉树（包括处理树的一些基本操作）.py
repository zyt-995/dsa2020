#二叉树 文本二叉树（包括处理树的一些基本操作）
class Tree:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
    def addleft(self,left):
        self.left=left
    def addright(self,right):
        self.right=right
    def pre(self,op):
        op(self)
        if self.left:
            self.left.pre(op)
        if self.right:
            self.right.pre(op)
    def mid(self,op):
        if self.left:
            self.left.mid(op)
        op(self)
        if self.right:
            self.right.mid(op)
    def pro(self,op):
        if self.left:
            self.left.pro(op)
        if self.right:
            self.right.pro(op)
        op(self)
def buildtree(g):#g为二阶矩阵
    s=[]#维护一个栈来处理父节点问题
    for line in g:
        level=0
        for i in line:
            if i=='\t':
                level=level+1
            else:
                break
        if level==0:
            root=Tree(line[level])
            s.append(root)    
        else:
            while len(s)>level:
                s.pop()
            father=s[-1]
            if line[level]=='*':
                father.addleft(Tree(None))
            else:
                if father.left!=None:
                    node=Tree(line[level])
                    father.addright(node)
                    s.append(node)
                else:
                    node=Tree(line[level])
                    father.addleft(node)
                    s.append(node)
    return root
g=[]
while True:
        line = input().rstrip('\n')
        if not line:
            break
        else:
            g.append(line)
root=buildtree(g)
#标准的使用lambda函数去输出数字
root.pre(lambda x: print(x.value, end='') if x.value is not None else None)
print()
root.mid(lambda x: print(x.value, end='') if x.value is not None else None)#意思是，如果if满足,就执行if前面的语句，不满足就执行else的语句
print()
root.pro(lambda x: print(x.value, end='') if x.value is not None else None)
