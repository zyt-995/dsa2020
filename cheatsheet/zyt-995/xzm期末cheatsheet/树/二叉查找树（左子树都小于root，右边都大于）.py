class Tree:
    def __init__(self,value,left=None,right=None):
        self.value,self.left,self.right=value,left,right
    def insert(self,node):
        if self.value==None:
            self.value=node.value
            return
        if node.value==self.value:
            return
        elif node.value<self.value:
            if self.left==None:
                self.left=node
            else:
                return self.left.insert(node)
        else:
            if self.right==None:
                self.right=node
            else:
                return self.right.insert(node)
    def pre(self):
        result=[]
        result.append(self.value)
        if self.left:
            result.extend(self.left.pre())
        if self.right:
            result.extend(self.right.pre())
        return result
s=list(map(int,input().split()))
root=Tree(None)
for value in s:
    node=Tree(value)
    root.insert(node)
answer=root.pre()
result=list(map(str,answer))
print(' '.join(result))
                
